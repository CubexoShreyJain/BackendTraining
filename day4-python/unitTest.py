import unittest

class TestClass(unittest.TestCase):

    def setUp(self): #To setup the environment
        pass

    def test_equal(self):
        self.assertEqual('s'+'h'+'r', 'shr')
    
    def test_truth(self):
        self.assertTrue('shre'.islower())
        self.assertTrue('df12'.isalnum())
        # self.assertTrue('sdaf'.isnumeric())
    def test_split(self):         
        s = 'hello world'
        # s = 234
        self.assertEqual(s.split(), ['hello', 'world']) 
        with self.assertRaises(TypeError): 
            s.split(2) 

if __name__ == "__main__":
    unittest.main()