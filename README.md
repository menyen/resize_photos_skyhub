# resize_photos

This is a simple webservice that consumes another webservice and produces a json with urls to images in different sizes.

### The challenge

• Consume a webservice endpoint (http://54.152.221.29/images.json) that returns a JSON of

photos. There are 10 photos.

• Generate three different formats for each photo. The dimensions are: small (320x240), 

medium (384x288) and large (640x480).

• Write a webservice endpoint that lists (in JSON format) all the ten photos with their 

respective formats, providing their URLs.

### Why Python?

Python offers many tools and frameworks built in the language. We don't need to worry about setting up the dev environment as all the modules are easy to install and run. The only concern is actually coding the program.

### Running the server

Before getting the webservice up and running, make sure you have the following python packages installed:
* Python 3 (Without this, nothing is gonna work)
* Flask-Pymongo (Python framework to create simple webservices and also connects to mongodb)
* Requests (Its only purpose is to make a request to the other webservice)
* Pillow (Image manipulation)

Now that everything is set, just go to where resize_photos.py is located and run **python resize_photos.py**.
Go to your browser and access **http://localhost:5000/json_imgs/** to get the json.

**Obs:** This repository has been commited with a virtual env in case you don't want to download all the necessary packages, so if you want to just run the code, activate the virtual env by running **source flask_ws/bin/activate** inside resize_photos_skyhub folder

### Automated tests
