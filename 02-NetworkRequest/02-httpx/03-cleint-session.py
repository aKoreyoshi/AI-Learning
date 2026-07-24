"""
   :author: Kairos
   :description: 对比 httpx.Client() 和 requests.Session()
   :version: 1.0
   :date: 2026年07月24日,18:51:20
 """

"""
    首先，先讲结论，session 和 client 定位其实是一样的。
    可以用来保存用户的信息，以保证连续访问
"""

data = {
    "username": "admin",
    "password": "123456"
}

import requests

# 初始形式
# 发起登录请求
response1 = requests.post(
    "https://example.com/login",
     json=data
)

# 此时登录请求已经结束
# 当再次发起请求获取用户信息时，这里没有cookie，会返回401
response2 = requests.get(
    "https://example.com/user/info",
)

"""
    问题：登录成功后，再次发起请求获取用户信息时，会返回401
"""
# 所以，使用session对象来保存cookie
# 创建一个session对象，请求完成之后，session对象自动保存cookie、headers等信息
session = requests.Session()

# session对象在登录成功后，会保存cookie
session.post(
    "/login",
    json=data
)

# 当再次发起请求时，会自动携带cookie
session.get("/user/info")
# 后续通过当前session对象发起请求，都会共享这些信息

# -------------------------------------------------------------------------------------------------------

# httpx 也是类似的情况
import httpx

# 初始形式
# 第一次发起登录请求
response3 = httpx.post(
    "https://example.com/login",
    json=data
)

# 此时登录请求已经结束,再次发起请求获取用户信息时，这里仍没有cookie，会返回401
response4 = httpx.get("https://example.com/user/info")

"""
    问题：登录成功后，再次发起请求获取用户信息时，还是缺少cookie，会返回401
"""

# 所以在使用httpx时，会创建一个client对象

with httpx.Client(base_url="https://example.com") as client:
    # client对象在登录成功后，会保存cookie等信息
    client.post(
        "/login",
        json=data
    )

    # 当再次发起请求时，会自动携带cookie
    client.get("/user/info")

"""
    总结： client是一个客户端对象，它负责着维护整个客户端的状态(连接、Cookie、Header、配置等)
"""