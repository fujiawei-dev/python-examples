import asyncio
import time


async def hello():
    print("Hello ...")
    time.sleep(1)
    print("... World!")


async def main():
    await asyncio.gather(hello(), hello())


async def hello_async():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


async def main_async():
    await asyncio.gather(hello_async(), hello_async())


print("time.sleep")
asyncio.run(main())

print("asyncio.sleep")
asyncio.run(main_async())
