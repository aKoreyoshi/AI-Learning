"""
   :author: Kairos
   :description: 在默认情况下，如果出现异常，则会立即终止
   :version: 1.0
   :date: 2026年07月27日,18:32:24
 """

import asyncio

async def task1():
    await asyncio.sleep(1)
    return "task1 执行完成..."

async def task2():
    await asyncio.sleep(2)
    raise Exception("task2 抛出一个异常...")

async def task3():
    await asyncio.sleep(3)
    return "task3 执行完成..."

async def main():
    # 默认情况下，如果出现异常，则会立即终止
    results = await asyncio.gather(
        task1(), task2(), task3()
    )
    print(results)

# asyncio.run(main())

async def main2():
    # 将gather参数 return_exceptions=True, 则异常会返回给调用者
    results = await asyncio.gather(
        task1(), task2(), task3(),
        return_exceptions=True
    )
    print(results)

asyncio.run(main2())