"""
   :author: Kairos
   :description: 程序主入口
   :version: 1.0
   :date: 2026年07月28日,18:07:46
 """

from fastapi import FastAPI
from routers import user

app = FastAPI(
    title="User Management API",
    version="1.0.0"
)

# 将路由注册到app中
app.include_router(
    user.router
)

@app.get("/")
async def root():
    return {
        "message": "FastAPI is running..."
    }