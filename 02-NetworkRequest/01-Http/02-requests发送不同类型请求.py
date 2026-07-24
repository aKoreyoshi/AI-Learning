"""
   :author: Kairos
   :description: 利用requests，尝试发送不同类型的请求
   :version: 1.0
   :date: 2026年07月24日,13:50:33
 """

import requests
# 1、GET请求
# 1.1 没有参数的GET请求
# response = requests.get("https://httpbin.org/get")
# print(response.status_code)     # 200
# print(response.text)

# 1.2 带参数的GET请求
params = {
    "name": "Kairos",
    "age": 18
}
# response2= requests.get("https://httpbin.org/get", params=params)
# print(response2.url)        # https://httpbin.org/get?name=Kairos&age=18
# print(response2.text)       # args 参数不在为空，响应结果中会包含我们请求的参数

#-------------------------------------------------------------------------------------

# 2、POST请求
# 2.1 无参数的POST请求
# response3 = requests.post("https://httpbin.org/post")
# print(response3.status_code)
"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "0", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.34.2", 
    "X-Amzn-Trace-Id": "Root=1-6a62ff4a-5df4a8cb6568cd5147e45def"
  }, 
  "json": null, 
  "origin": "203.27.106.146", 
  "url": "https://httpbin.org/post"
}
"""
# print(response3.text)

# 2.2 带参数的POST请求
data = {
    "username": "admin",
    "password": "123456"
}
# 使用json参数，自动将dict转换成json格式，并会自动设置Content-Type为application/json
# response4 = requests.post("https://httpbin.org/post", json=data)
response4 = requests.post("https://httpbin.org/post", data=data)
print(response4.text)