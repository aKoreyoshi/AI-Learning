"""
   :author: Kairos
   :description: 对比同步和异步，异步到底快在哪里？
   :version: 1.0
   :date: 2026年07月27日,17:42:35
 """

import time
import asyncio
import httpx

# 我们要利用python中最精确的计时器之一：time.perf_counter()

# 同步

def fetch(url):
    response = httpx.get(url)
    return response.status_code

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
]

start = time.perf_counter()
print(f"同步开始... ---{start}")

for url in urls:
    status_code = fetch(url)
    print(status_code)

end = time.perf_counter()
print(f"同步结束... ---{end}")

print(f"同步耗时: {end - start:.2f}秒")

# -----------------------------------------------------------------------------------------------

# 异步

async def fetch2(client, url):
    response = await client.get(url)
    return response.status_code

async def main():

    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
    ]

    async with httpx.AsyncClient() as client:

        tasks = [
            asyncio.create_task(
                fetch2(client, url)
            )
            for url in urls
        ]

        responses = await asyncio.gather(*tasks)
        print(responses)

start = time.perf_counter()
print(f"异步开始... ---{start}")

asyncio.run(main())

"""
    总结: 真正快的是，等待时间被重叠(overlap)了
"""

end = time.perf_counter()
print(f"异步结束... ---{end}")

print(f"异步耗时: {end - start:.2f}秒")

