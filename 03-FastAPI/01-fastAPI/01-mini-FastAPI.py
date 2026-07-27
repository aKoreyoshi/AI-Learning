"""
   :author: Kairos
   :description: 尝试简单实现一下FastAPI的原理
   :version: 1.0
   :date: 2026年07月28日,00:14:26
 """

class my_FastAPI:

    def __init__(self):
        self.routes = {}



    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator


app = my_FastAPI()

@app.get("/")
def hello():
    return "hello world"


# 模拟运行
func = app.routes["/"]
result = func()
print(result)       # hello world