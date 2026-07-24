"""
   :author: Kairos
   :description: 初步认识 httpx
   :version: 1.0
   :date: 2026年07月24日,15:47:20
 """

import httpx

# 获取httpx的版本号
print(httpx.__version__)

# 发起第一个httpx请求
# response = httpx.get("https://httpbin.org/get")

# 响应结果和requests一样
# print(response)                 # <Response [200]>
# print(response.status_code)
# print(response.text)
# print(response.json())


# 发起带参数的请求
params = {
    "name": "Kairos",
    "age": 25
}
response = httpx.get("https://httpbin.org/get", params=params)
print(response.text)
