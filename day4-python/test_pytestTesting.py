import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5
   assert num*num == 625

def testsquare():
   num = 7
   assert 7*7 == 40 #assert returns true if expression matches, else return exception

def tesequality():
   assert 10 == 11