# 简单来说，带参数的装饰器，其实就是在原本的装饰器外层套了一层函数，然后这个最外层的函数有一个返回值，就是装饰器本身
def permission(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("before")
            print(f"装饰器当前传入的参数是: {role}")
            func(*args, **kwargs)
            print("after")
        return wrapper
    return decorator


@permission("admin")
def add_user():
    print("添加用户")


add_user()