import asyncio
import random
import time

async def washing_machine():
    
    for i in range(3):
        print("Doing washing machine")
        time.sleep(2) # Do a 2 sec task, 3 times
        await asyncio.sleep(10) # Sleep for 10 sec

async def kids():
    
    for i in range(24):
        print("Doing kids")
        time.sleep(3) # Do a 3 sec task, 3 times
        await asyncio.sleep(random.randint(2,12)) # Sleep for random sec

async def check_book():
    
    for i in range(10):
        print("Doing checkbook")
        await asyncio.sleep(1) # Sleep for random sec

async def parents():
    await asyncio.gather(kids(), washing_machine(), check_book())
    
asyncio.run(parents())


