"""
   :author: Kairos
   :description: 事件循环 Event Loop
   :version: 1.0
   :date: 2026年07月27日,16:25:50
 """

import asyncio
import time

async def hello():
    print("Start...")

    # await asyncio.sleep(2)
    time.sleep(2)

    print("End...")

asyncio.run(hello())

"""
    asyncio.run() 就是创建了一个 Event Loop
    事件循环(Event Loop) 就相当于是一个管理员，负责着协程的调度、执行等；
    await 关键词就是告诉 Event Loop, 你先去执行执行其他协程，等待结束后再恢复当前协程；
"""
