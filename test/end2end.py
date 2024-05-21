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

    test_request = HTTPSession('http', '127.0.0.1', 9090)
    unittest.main()
