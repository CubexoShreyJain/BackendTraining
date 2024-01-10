import unittest
from mySum import mySumFunc

class TestSum(unittest.TestCase):
    def test_variable_args(self):
        self.assertEqual(mySumFunc(10,10,10), 30)
    
    # def test_list(self): #ERROR
    #     self.assertEqual(([12,12, 12]), 36)import
        
    # def test_tuple(self): #ERROR
    #     self.assertEqual(mySumFunc((12,12, 12, 10)), 46)
        
    def test_supply(self):
        l = [5,5,5,5]
        self.assertEqual(mySumFunc(*l), 20)
        
    def test_boolT(self):
        self.assertTrue("Shrey".isalpha())
    def test_boolF(self): 
        self.assertFalse("Shrey".isnumeric())
    def test_is(self):
        x = 257
        y = 257
        # self.assertIs(mySumFunc(250,10), 260) #Fail
        self.assertIsNot(mySumFunc(250,10), 260) 
    def test_in(self):
        self.assertIn(mySumFunc(50+50), [50,100,150,200])
    def test_none(self):
        self.assertIsNone(mySumFunc())
    def test_instance(self):
        self.assertIsInstance(self, TestSum)
    
if __name__ == "__main__":
    unittest.main()