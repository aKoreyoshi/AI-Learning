"""
   :author: Kairos
   :description: response.raise_for_status()帮助我们处理异常请求
   :version: 1.0
   :date: 2026年07月24日,14:36:12
 """

import requests

# response = requests.get("https://httpbin.org/status/404")

# print(response.text)
# 如果请求响应码不是200，则抛出异常，实则是将http响应异常转换为python异常
# response.raise_for_status()


# 结合try except语句处理异常
try:
    response = requests.get("https://httpbin.org/status/404")

    response.raise_for_status()

    data = response.json()

except requests.exceptions.HTTPError as e:
    print(f"HTTP异常: {e}")

