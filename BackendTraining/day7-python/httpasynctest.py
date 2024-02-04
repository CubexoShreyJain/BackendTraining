import asyncio
import aiohttp
from random import random

semaphore = asyncio.Semaphore(10)

async def getres(sess: aiohttp.ClientSession, url: str):
    
    async with semaphore:
        async with sess.get(url) as _res:
            await asyncio.sleep(random())
        
        if ("random" in url):
            print("R", flush=True, sep="", end="")
        else:
            print("O", flush=True, sep="", end="")
    

async def main(urls: list[str]):
    
    async with aiohttp.ClientSession() as sess:
        tasks = []
        for url in urls:          
            task = asyncio.create_task(getres(sess, url))
            tasks.append(task)
        
        await asyncio.gather(*tasks)
    

urls = ["https://andruxnet-random-famous-quotes.p.rapidapi.com/",
        "https://omgvamp-hearthstone-v1.p.rapidapi.com/info"]*40

asyncio.run(main(urls))

