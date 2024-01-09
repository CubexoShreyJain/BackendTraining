# def testFunc():
#     print("Entered the function")
#     x = 4+5
#     yield x
#     x-=4
#     print("Passed A")
#     yield 8
    
# test = testFunc()

# print(next(test))
# print(next(test))

import asyncio

async def func1():
    print("entered func1")
    print("2")
    await asyncio.sleep(1)
    print("3")
    await asyncio.sleep(1)
    print("4")

async def func2():
    print("5")
    await func1()
    print("6")

async def main():
    print("Main")
    task  = asyncio.create_task(func1())
    print("main2")
    await asyncio.sleep(1)
    print("final")
    # await asyncio.sleep(1)
    print("double final")
    
async def main2():
    print ("Main 2 started")

    task = await asyncio.gather(func1(), func2(), main())
    print ("Main 2 ended")
asyncio.run(main2())