import unittest

class TestSum(unittest.TestCase):

    def test_supply(self):
        name = "Shrey"
        self.assertEqual(name, "Shrey")
    
if __name__ == "__main__":
    unittest.main()