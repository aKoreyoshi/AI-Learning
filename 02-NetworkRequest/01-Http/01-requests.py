"""
   :author: Kairos
   :description: 通过requests，发送http请求
   :version: 1.0
   :date: 2026年07月24日,11:43:41
 """

# 简单尝试requests发送请求
import requests

res = requests.get("https://httpbin.org/get")
print(type(res))        # <class 'requests.models.Response'>
print(res.text)   # <class 'str'>

# 上面text 返回的是字符串，如果想将其转换成字典，可以使用json()方法
print(type(res.json()))
print(res.json())       # <class 'dict'>

content = res.json()
print(content["headers"]["User-Agent"])
print(res.content)


