"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月27日,16:43:42
 """
import asyncio
import time

async def work(name, seconds):
    print(f"{name} is working...")

    # await asyncio.sleep(seconds)
    time.sleep(seconds)         # 换成time.sleep，会导致程序阻塞，直到任务完成

    print(f"{name} is done.")


# 方式一: 但是不推荐这种写法
"""
    结果:
        A is working...
        B is working...
        C is working...
        C is done.
        A is done.
        B is done.
    
"""
async def main():
    task1 = asyncio.create_task(work("A", 2))
    task2 = asyncio.create_task(work("B", 3))
    task3 = asyncio.create_task(work("C", 1))

    await task1
    await task2
    await task3

# asyncio.run(main())

# -----------------------------------------------------------------------------------------------------------

# 方式二: 推荐这种写法
async def main2():
    task1 = asyncio.create_task(work("Task1", 2))
    task2 = asyncio.create_task(work("Task2", 3))
    task3 = asyncio.create_task(work("Task3", 1))

    await asyncio.gather(task1, task2, task3)

asyncio.run(main2())

"""
    总结：
        协程(Coroutine)描述“要做什么”  Task描述“正在做什么”  Event Loop决定“什么时候做”
"""
