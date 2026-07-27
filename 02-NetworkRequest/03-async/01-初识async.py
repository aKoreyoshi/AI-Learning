"""
   :author: Kairos
   :description: 初识python异步编程
   :version: 1.0
   :date: 2026年07月27日,16:03:34
 """

import asyncio

"""
    以前: def func() 创建的是 Function 对象
    现在: async def func() 创建的是 Coroutine Function(协程函数)
"""
async def hello():
    print("Hello World!")


# 直接调用，会报错 -> RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# hello()

print(type(hello))  # <class 'function'>

# 这时候函数并未直接执行，而是返回了一个协程对象
result = hello()
print(type(result)) # <class 'coroutine'>