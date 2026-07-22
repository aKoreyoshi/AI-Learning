def decorator(func):

    # *args - 位置参数列表，可变参数
    # **kwargs - 关键字参数列表，可变参数
    def wrapper(*args, **kwargs):
        print("before")
        return func(*args, **kwargs)
    return wrapper


def login(username, password):
    print("登录成功")
    print(f"用户名是: {username}")
    print(f"密码是: {password}")


# 装饰器调用方法一:
new_login = decorator(login)
new_login("admin", "123456")


# 装饰器调用方法二:
@decorator
def login2(username, password):
    print("登录成功")
    print(f"用户名是: {username}")
    print(f"密码是: {password}")

login2("macong", "20010419")