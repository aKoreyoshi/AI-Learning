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

# 几种参数类型
# params / data / json
"""
    params: 位置在URL之后，没有content-type，一般在 GET 方法中使用，主要做 查询 操作
    data:   位置在body(请求体)中，content-type为表单形式，一般在 POST 方法中使用，主要是 提交表单 操作
    json:   位置在body(请求体)中，content-type为json形式，一般在 POST、PUT 方法中使用，主要是API数据交互
"""