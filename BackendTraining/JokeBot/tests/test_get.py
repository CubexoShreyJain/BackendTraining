import requests
from requests.exceptions import HTTPError
from JokeBot.constants import URL
import unittest

class TestGET(unittest.TestCase):
    
    def test_type(self):
        self.assertEqual(requests.get(URL).headers['content_type'], 'application/json; charset=UTF-8')
    
    def test_success(self):
        self.assertEqual(requests.get(URL + 'Any').status_code, 200) # Good flow
        self.assertEqual(requests.get(URL + 'xyz').status_code, 200) # Bad flow
    
    def test_response(self):
        self
    