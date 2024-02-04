import requests 
import os
import sys
# from constants.constants import *

# constants = os.path.dirname(__file__)
# JokeBot = os.path.abspath(os.path.join(constants,'..'))
# sys.path.append(JokeBot)
from JokeBot.constants import URL

# def getAnyJoke():
#     res = requests.get(URL+ 'Any?type=single').json()
#     if not (res['error']):
        # return res['setup']
            
def getJoke(category = "Any"):
    res = requests.get(URL+ f'{category}?type=single').json()
    if not (res['error']):
        return res['setup']
    
            
            
if __name__ == '__main__':
    print(getJoke())
    print( requests.get(URL+ 'Any?type=single').json())