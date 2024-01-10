import myapp
import unittest

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        myapp.app.testing = True    
        self.app = myapp.app.test_client() # Setting test client
    
    def test_homePage(self):
        result = self.app.get('/') # Check Routes
        