"""
    根据上节内容，使用装饰器会改变函数的身份。
    那么现在我们就通过 functools.wraps 来解决这个问题
"""

from functools import wraps

def decorator(func):

    # 使用 wraps 来解决这个问题,在这里 wraps 也是一个装饰器，即装饰器也能装饰装饰器
    # 这里的 wraps 会保留被装饰函数的元信息
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("开始")
        func(*args, **kwargs)
        print("结束")
    return wrapper

@decorator
def hello():
    print("hello")

# 测试
# 在使用了 decorator 之后，打印函数的元信息，可以看到，函数名没有被修改
# 真正的原因： wraps 并未将 wrapper变为原函数，而是把原函数的大部分元数据复制给 wrapper
print(hello.__name__)   # hello
print(hello.__doc__)    # None
help(hello)             # Help on function hello in module __main__:   hello()
hello.__wrapped__()     # 输出结果是原函数的结果
