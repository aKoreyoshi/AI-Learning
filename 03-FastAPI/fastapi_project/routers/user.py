"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,18:11:21
 """

from fastapi import APIRouter, HTTPException, Depends
from schemas.user import UserCreate, UserResponse, UserLogin
from services import user_service
from dependencies import get_current_user
from schemas.common import ResultModel


# 创建一个路由
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/list")
async def get_users():
    return user_service.users


# 用户注册 (统一返回结果)
@router.post(
    "/register",
    response_model=ResultModel,
)
async def register(user: UserCreate):

    result = user_service.register_user(user)
    return ResultModel(data=result)

# 用户登录
@router.post("/login", response_model=ResultModel)
async def login(user: UserLogin):
    result = user_service.login_user(user)
    return ResultModel(message="登录成功")


# 获取当前用户信息
@router.get("/profile", response_model=UserResponse)
async def profile(
        user = Depends(get_current_user)
    ):
    return user


# 查询用户信息(统一返回结果)
@router.get(
    "/{user_id}",
    response_model=ResultModel
)
async def get_user(user_id: int):

    result = user_service.get_user_byid(user_id)
    return ResultModel(data=result)