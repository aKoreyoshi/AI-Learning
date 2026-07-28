"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,15:23:34
 """

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# 接收数据 pydantic 会验证数据并封装成 User 对象
@app.post("/user")
async def create_user(user: User):
    return user
