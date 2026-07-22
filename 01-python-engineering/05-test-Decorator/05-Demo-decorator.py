def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"第 {i+1} 次执行")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@retry(3)
def hello(name):
    print(f"hello {name}")
    return 100


result = hello("Mac")
print(result)