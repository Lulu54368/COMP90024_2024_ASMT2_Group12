import unittest
import requests
import json
from unittest.mock import patch

class HTTPSession:
    def __init__(self, protocol, hostname, port):
        self.session = requests.Session()
        self.base_url = f'{protocol}://{hostname}:{port}'

    def get(self, path):
        return self.session.get(f'{self.base_url}/{path}')

    def post(self, path, data):
        return self.session.post(f'{self.base_url}/{path}', data)

    def put(self, path, data):
        return self.session.put(f'{self.base_url}/{path}', data)

    def delete(self, path):
        return self.session.delete(f'{self.base_url}/{path}')

class TestEnd2End(unittest.TestCase):
    def test_mastodon(self):
        self.assertEqual(test_request.get('/mastodon/gt').status_code, 200)
        self.assertIsNotNone(test_request.get('/mastodon/gt').json())

        self.assertEqual(test_request.get('/mastodon/lt').status_code, 200)
        self.assertIsNotNone(test_request.get('/mastodon/lt').json())

        self.assertEqual(test_request.get('/mastodon/count').status_code, 200)
        self.assertIsNotNone(test_request.get('/mastodon/count').json())

    def test_twitter(self):
        self.assertEqual(test_request.get('/twitter/lt').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/lt').json())

        self.assertEqual(test_request.get('/twitter/gt').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/gt').json())

        self.assertEqual(test_request.get('/twitter/count').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/count').json())

        self.assertEqual(test_request.get('/twitter/sentiment').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/sentiment').json())


if __name__ == '__main__':

    test_request = HTTPSession('http', 'localhost', 9090)
    unittest.main()
