# resize_photos.py
import io
import os
import urllib
import requests
from PIL import Image
from flask import Flask, jsonify, request, send_from_directory, url_for
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename



app = Flask(__name__, static_folder='imgs/')

app.config["MONGO_DBNAME"] = 'wsdb'
app.config["MONGO_URI"] = 'mongodb://localhost:27017/wsdb'

mongo = PyMongo(app)

# this can be changed to whatever other webservice that provides json as input
consumed_url = 'http://54.152.221.29/images.json'
consumer_url = 'http://localhost:5000'

# these sizes can be changed if needed to
sizes = [
    {
        "dimension": (320, 240),
        "prefix": "small_"
    },
    {
        "dimension": (384, 288),
        "prefix": "medium_"
    },
    {
        "dimension": (640, 480),
        "prefix": "large_"
    }
]

@app.route('/', methods=['GET'])
def return_imgs_json():
    """Consumes a webservice and creates images in different sizes for each entry in the json returned by the
    consumed webservice

    :return: a json containing urls for images in different sizes
    """
    consume_imgs_json()
    imgs = mongo.db.imgs
    output = []
    for img in imgs.find():
        output.append({'url': img['url'], 'small': img['small'], 'medium': img['medium'], 'large': img['large']})
    return jsonify({'images': output})


@app.route("/imgs/<filename>/")
def images(filename):
    """Returns the image in the webservice

    :param filename:
    :return: image shown in browser
    """
    return send_from_directory(app.static_folder, filename)


def consume_imgs_json():
    """Stores urls in mongodb"""
    imgs = mongo.db.imgs
    r = requests.get(consumed_url)
    input = r.json()
    for e in input['images']:
        json_imgs = generate_sizes_from_url_img(e['url'])
        urls_obj = {
            'url': json_imgs['url'],
            'small': json_imgs['small'],
            'medium': json_imgs['medium'],
            'large': json_imgs['large']
        }
        # makes sure the url object won't be inserted again in db
        if imgs.find(urls_obj).count() <= 0:
            imgs.insert(urls_obj)


def generate_sizes_from_url_img(url):
    """Given an image url, it will store the file locally and it will also create three copies with different sizes

    :param url:
    :return: dictionary containg the url for each image created
    """
    url_sizes = {}
    response = urllib.request.urlopen(url)  # opening url

    # saving file locally
    image_file = io.BytesIO(response.read())
    img = Image.open(image_file)
    filename = secure_filename(url.rpartition('/')[-1])
    img_location = os.path.join(app.static_folder, filename)
    img.save(img_location, format='JPEG')
    url_sizes['url'] = '{}{}'.format(consumer_url, url_for('images', filename=filename))

    # for each image size, creates a copy with given dimensions in sizes array
    for element in sizes:
        create_img_custom_size(img, element["dimension"], filename, element["prefix"], url_sizes)

    return url_sizes


def create_img_custom_size(img, size, filename, prefix, url_sizes):
    """Generate a new image with custom sizes

    :param img:
    :param size:
    :param filename:
    :param prefix:
    :param url_sizes:
    :return:
    """
    new_img = img.resize(size)
    new_img_filename = '{}{}'.format(prefix, filename)
    new_img_location = os.path.join(app.static_folder, new_img_filename)
    new_img.save(new_img_location, format='JPEG')
    url_sizes[prefix[:-1]] = '{}{}'.format(consumer_url, url_for('images', filename=new_img_filename))

if __name__ == '__main__':
    app.run(debug=True)
