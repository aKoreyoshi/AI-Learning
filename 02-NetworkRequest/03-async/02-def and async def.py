"""
   :author: Kairos
   :description: 比较普通函数和异步函数
   :version: 1.0
   :date: 2026年07月27日,16:14:50
 """

import asyncio

# 普通函数
def hello():
    print("Hello World!")

result1 = hello()

print(result1)          # None
print(type(result1))    # <class 'NoneType'>


# 异步函数 - 协程函数
async def hello():
    print("Hello World!")

result2 = hello()

print(result2)          # <coroutine object hello at 0x0000020E0D5EA7C0>
print(type(result2))    # <class 'coroutine'>

"""
    普通函数 会打印输出结果，而 异步函数 没有任何输出.
    总结:
        "async def" 定义的是一个协程函数，而直接调用它不会立即执行，只会返回一个 “协程对象”，
        真正的代码执行是由 “事件循环(Event Loop)” 来调度的。
"""