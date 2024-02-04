import asyncio
import random
import time

async def washing_machine():
    
   
    for i in range(2):
        time.sleep(1)
        print("into machine")
        await asyncio.sleep(1)
        
async def kids():
  
    
    for i in range(2):
        time.sleep(1)
        print("into kids")
        await asyncio.sleep(4)

async def check():
    
    
    for i in range(2):
        time.sleep(1)
        print("into check")
        await asyncio.sleep(.1)



async def parents():
    # await asyncio.gather(kids(), washing_machine(), check())
    t1 = asyncio.create_task(kids())
    t2 =  asyncio.create_task(washing_machine())
    t3 = asyncio.create_task(check())
    
    await t1 # Running just one, does the job
    await t2
    await t3
  
        
    print("\n\nTHIS\n\n")
    
asyncio.run(parents())
