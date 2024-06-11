import asyncio

async def func1():
    print("Task1 started")
    await asyncio.sleep(20)
    print("Task1 Ended")

async def func2():
    print("Task2 started")
    await asyncio.sleep(10)
    print("Task2 Ended")

async def main():
    L = await asyncio.gather(
    func1(),
    func2(),
    )
    print("Main")

asyncio.run(main())

