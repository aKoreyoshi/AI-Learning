def decorator(func):
    def wrapper():
        print("开始执行")
        func()
        print("执行结束")
    return wrapper


def login():
    print("登录成功")

login2 = decorator(login)

login2()