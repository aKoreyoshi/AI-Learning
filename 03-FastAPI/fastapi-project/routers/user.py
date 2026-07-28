"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,18:11:21
 """

from fastapi import APIRouter, HTTPException
from schemas.user import (UserCreate, UserResponse)
from services import user_service


# 创建一个路由
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/list")
async def get_users():
    return user_service.users


# 用户注册
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
async def register(user: UserCreate):
    return user_service.register_user(user)


# 查询用户信息
@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_user(user_id: int):
    return user_service.get_user_byid(user_id)