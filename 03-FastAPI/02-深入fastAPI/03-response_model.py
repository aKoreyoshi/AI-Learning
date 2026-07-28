"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,16:33:05
 """

from fastapi import FastAPI
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str

app = FastAPI()


# 响应模型 response_model, 返回的json数据会按照这个模型进行格式化
@app.get("/user", response_model=UserResponse)
async def get_user():
    return {
        "id": 1,
        "name": "Kairos",
        "password": "macong"
    }