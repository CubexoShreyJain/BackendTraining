import unittest

class TestingTest(unittest.TestCase):
    
    t = (34,423,1,34,12,34,1234)
    
    def test_sum(self):
        self.assertEqual(sum([12,10,10]), 32, "YOU DUMB ASS")
        
    def test_tuple(self):
        self.assertEqual(self.t[0], 32, "Good Work")

# if __name__ == "__main__":
#     unittest.main()