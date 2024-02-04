import asyncio
import aiofiles
import requests

async def read_file(file_path):
    # Open file asynchronously
    async with aiofiles.open(file_path, 'r') as file:
        # Read content asynchronously
        content = await file.read()
        return content
    
async def other_task():
    # Do other non-blocking tasks while waiting for file reading to complete
    for i in range(5):
        print(f"Doing other tasks {i}...")
        await asyncio.sleep(1)

# async def get_joke():
#     for i in range(5):
#         x = await requests.get("https://v2.jokeapi.dev/joke/Any")
#         print(x)

async def main():
    file_path = 'example.txt'

    # Schedule the read_file coroutine to run asynchronously
    task = asyncio.create_task(read_file(file_path))
    task2 = asyncio.create_task(other_task())
    # task3 = asyncio.create_task(get_joke())

    
    # Wait for the file reading to complete
    file_content = await task
    await task2
    # await task3

    # Process the file content
    print(f"File content: {file_content}")

# Run the event loop
asyncio.run(main())
