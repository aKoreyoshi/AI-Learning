"""
   :author: Kairos
   :description: 认识httpx.Client()
   :version: 1.0
   :date: 2026年07月24日,17:47:43
 """

import httpx

# 方式一: 直接创建
# 创建client对象 -> 起到“连接复用”的作用，创建一次，复用多次，避免每次请求重新创建TCP连接
# client = httpx.Client()
#
# response = client.get("https://httpbin.org/get")
# print(response)
#
# # 注意，创建的client对象，必须调用close()方法，才会关闭TCP连接
# client.close()


# 方式二: 使用with语句(推荐)
# 离开with语句时，会自动调用close()方法，关闭TCP连接，不需要手动调用close()
with httpx.Client() as client:
    response = client.get("https://httpbin.org/get")
    print(response.text)



# 还可以通过client对象来保存一些公共配置，比如headers、cookies、params等
headers = {
    "authorization": "Bearer 123456"
}
base_url = "https://api.xxx.com"
with httpx.Client(headers=headers, base_url=base_url) as client:

    # 发送POST请求登录，client保存cookies
    client.post(
        "/login",
        json={"username": "admin", "password": "123456"})

    # 后续接着访问用户列表
    response = client.get("/users")
    print(response.text)