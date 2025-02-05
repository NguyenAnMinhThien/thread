import asyncio
import time


async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")


async def main():
   await asyncio.gather(
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
    )
   print("Main Ended..")


start = time.time()
asyncio.run(main())
end = time.time()
print(end - start)
