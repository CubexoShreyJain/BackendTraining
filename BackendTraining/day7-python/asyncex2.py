import asyncio
import time

async def userInp(x):
    return int(input(x))

async def driver():
    
    print("Welcome to our shop")
    x = await userInp("Please enter your age: ")
   
    if (x<18):
        print("Sorry! you can't access this site.")
        cnf = await userInp("Do you want to change your age?: ")
        if (cnf> 18):
            await ageCfm()
    else:
        await ageCfm()

async def ageCfm():
    
    print("Welcome to the bad world!")

async def timepass():
    for i in range(1000):
        print("Doing timepass")
        await asyncio.sleep(.5)
    
async def main():
    # x = asyncio.create_task(driver())
    # y = asyncio.create_task(timepass())
    
    # await x
    # await y
    await asyncio.gather(driver(), timepass())

asyncio.run(main())
            
