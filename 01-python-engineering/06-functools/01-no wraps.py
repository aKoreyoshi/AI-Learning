# 测试在没有 wraps 的情况下，装饰器对函数的影响

# 定义一个装饰器
def permission(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"permission: {role}")
            func(*args, **kwargs)
            print("结束")
        return wrapper
    return decorator

# 定义一个函数  在没有装饰器的情况下，打印自身信息
def hello():
    print("hello")

print(hello.__name__)   # hello
print(hello.__doc__)    # None
help(hello)             # Help on function hello in module __main__:  hello()

# 定义第二个函数，使用装饰器
@permission("admin")
def hello2():
    print("hello world")

print(hello2.__name__)   # wrapper
print(hello2.__doc__)    # None
help(hello2)             # Help on function wrapper in module __main__:   wrapper(*args, **kwargs)