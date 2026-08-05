"""
   :author: Kairos
   :description: 用户数据结构
   :version: 1.0
   :date: 2026年07月28日,18:33:47
 """

from pydantic import BaseModel

# 创建用户
class UserCreate(BaseModel):
    username: str
    password: str

# 用户登录
class UserLogin(BaseModel):
    username: str
    password: str


# 用户响应
class UserResponse(BaseModel):
    id: int
    username: str


# 用户更新
class UserUpdate(BaseModel):
    username: str | None = None