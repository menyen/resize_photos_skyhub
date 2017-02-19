
import os
import unittest
import resize_photos
from flask import json
from werkzeug.utils import secure_filename


class TestResizePhotosWS(unittest.TestCase):

    def setUp(self):
        """Setting up variables"""
        # json containg the expected result from calling '/'
        self.json_expected_response = {
            "images": [
                {
                    "large": "http://localhost:5000/imgs/large_b737_5.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b737_5.jpg/",
                    "small": "http://localhost:5000/imgs/small_b737_5.jpg/",
                    "url": "http://localhost:5000/imgs/b737_5.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b777_5.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b777_5.jpg/",
                    "small": "http://localhost:5000/imgs/small_b777_5.jpg/",
                    "url": "http://localhost:5000/imgs/b777_5.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b737_3.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b737_3.jpg/",
                    "small": "http://localhost:5000/imgs/small_b737_3.jpg/",
                    "url": "http://localhost:5000/imgs/b737_3.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b777_4.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b777_4.jpg/",
                    "small": "http://localhost:5000/imgs/small_b777_4.jpg/",
                    "url": "http://localhost:5000/imgs/b777_4.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b777_3.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b777_3.jpg/",
                    "small": "http://localhost:5000/imgs/small_b777_3.jpg/",
                    "url": "http://localhost:5000/imgs/b777_3.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b737_2.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b737_2.jpg/",
                    "small": "http://localhost:5000/imgs/small_b737_2.jpg/",
                    "url": "http://localhost:5000/imgs/b737_2.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b777_2.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b777_2.jpg/",
                    "small": "http://localhost:5000/imgs/small_b777_2.jpg/",
                    "url": "http://localhost:5000/imgs/b777_2.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b777_1.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b777_1.jpg/",
                    "small": "http://localhost:5000/imgs/small_b777_1.jpg/",
                    "url": "http://localhost:5000/imgs/b777_1.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b737_4.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b737_4.jpg/",
                    "small": "http://localhost:5000/imgs/small_b737_4.jpg/",
                    "url": "http://localhost:5000/imgs/b737_4.jpg/"
                },
                {
                    "large": "http://localhost:5000/imgs/large_b737_1.jpg/",
                    "medium": "http://localhost:5000/imgs/medium_b737_1.jpg/",
                    "small": "http://localhost:5000/imgs/small_b737_1.jpg/",
                    "url": "http://localhost:5000/imgs/b737_1.jpg/"
                }
            ]
        }

        # creating test client which will make the requests
        self.app = resize_photos.app.test_client()

    def tearDown(self):
        basepath = os.path.dirname(__file__)
        for element in self.json_expected_response['images']:
            for key, value in element.items():
                filename = 'imgs/{}'.format(secure_filename(value[:-1].rpartition('/')[-1]))
                filepath = os.path.abspath(os.path.join(basepath, "..", filename))
                try:
                    os.remove(filepath)
                except OSError:
                    pass

    def test_request(self):
        """Should return status 200"""
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_request_content(self):
        """Should return the same json as json_expected_reponse"""
        rv = self.app.get('/')
        json_actual_response = json.loads(rv.data)
        self.assertEqual(json_actual_response, self.json_expected_response)

    def test_each_photo_url(self):
        """Should return status code 200 for all url found in json got from '/'"""
        for element in self.json_expected_response['images']:
            rv_url = self.app.get(element['url'])
            rv_small = self.app.get(element['small'])
            rv_medium = self.app.get(element['medium'])
            rv_large = self.app.get(element['large'])
            if not all(status_code == 200 for status_code in (rv_url, rv_small, rv_medium, rv_large)):
                self.assertNotEquals
        self.assertEquals

