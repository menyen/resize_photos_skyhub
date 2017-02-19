from flask import json
from flask import session
import flask
import flask_pymongo
import unittest
import resize_photos


class FlaskRequestTest(unittest.TestCase):

    def setUp(self):
        self.app = resize_photos.app.test_client()
        '''self.context = self.app.test_request_context('/')
        self.context.push()'''

    def tearDown(self):
        pass
        #self.context.pop()

    def test_request(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_request_content(self):
        expected_response = {
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
        rv = self.app.get('/')
        actual_response = rv.json
        self.assertEqual(actual_response, expected_response)



'''class FlaskPyMongoTest(FlaskRequestTest):

    def setUp(self):
        super(FlaskPyMongoTest, self).setUp()

        self.dbname = self.__class__.__name__
        self.app.config['MONGO_DBNAME'] = self.dbname
        self.mongo = flask.ext.pymongo.PyMongo(self.app)

    def tearDown(self):
        self.mongo.cx.drop_database(self.dbname)

        super(FlaskPyMongoTest, self).tearDown()

    def test_request(self):
        pass'''