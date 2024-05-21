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
        # Testing the mastodon (sentiment greater than 0)
        self.assertEqual(test_request.get('/mastodon/gt').status_code, 200)
        self.assertIsNotNone(test_request.get('/mastodon/gt').json())
        self.assertGreater(len(test_request.get('/mastodon/gt').json()), 0)
        # Testing the mastodon (sentiment less than 0)
        self.assertEqual(test_request.get('/mastodon/lt').status_code, 200)
        self.assertIsNotNone(test_request.get('/mastodon/lt').json())
        self.assertGreater(len(test_request.get('/mastodon/lt').json()), 0)
        # Testing the mastodon count
        self.assertEqual(test_request.get('/mastodon/count').status_code, 200)
        self.assertIsNotNone(test_request.get('/mastodon/count').json())
        

    def test_twitter(self):
        # Testing twitter (sentiment less than 0)
        self.assertEqual(test_request.get('/twitter/lt').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/lt').json())
        self.assertGreater(len(test_request.get('/twitter/lt').json()), 0)
        # Testing twitter (sentiment greater than 0)
        self.assertEqual(test_request.get('/twitter/gt').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/gt').json())
        self.assertGreater(len(test_request.get('/twitter/gt').json()), 0)
        # Testing count of twitter
        self.assertEqual(test_request.get('/twitter/count').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/count').json())
        self.assertEqual(int(test_request.get('/twitter/count').json()["count"]), 71566)
        # Testing average sentiment score by area
        self.assertEqual(test_request.get('/twitter/sentiment').status_code, 200)
        self.assertIsNotNone(test_request.get('/twitter/sentiment').json())
        self.assertGreater(len(test_request.get('/twitter/sentiment').json()), 0)
        
    def test_bom(self):
        self.assertEqual(test_request.get('/get-bom-list').status_code, 200)
        self.assertIsNotNone(test_request.get('/get-bom-list').text)
        
        self.assertEqual(test_request.get('/get-bom-name').status_code, 200)
        self.assertIsNotNone(test_request.get('/get-bom-name').text)
        
    def test_map(self):
        self.assertEqual(test_request.get('/get-map-region-info').status_code, 200)
        self.assertIsNotNone(test_request.get('/get-map-region-info').text)
        
    def test_population(self):
        self.assertEqual(test_request.get('/get-population-list').status_code, 200)
        self.assertIsNotNone(test_request.get('/get-population-list').text)

if __name__ == '__main__':

    test_request = HTTPSession('http', 'localhost', 9090)
    unittest.main()
