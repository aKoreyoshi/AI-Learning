"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,18:11:21
 """

from fastapi import APIRouter, HTTPException, Depends
from schemas.user import UserCreate, UserResponse, UserLogin
from services import user_service
from dependencies.auth import get_current_user
from schemas.common import ResultModel

from sqlalchemy.orm import Session
from database.database import get_db
from crud.user import create_user
from utils.jwt import create_access_token


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
    response_model=ResultModel[UserResponse]
    )
async def register(username: str, password: str, db: Session=Depends(get_db)):
    # 调用service方法注册用户
    user = user_service.register_user(db, username, password)
    return ResultModel(message="注册成功", data=UserResponse.model_validate(user))


# 用户登录
@router.post("/login", response_model=ResultModel)
async def login(user: UserLogin, db:Session = Depends(get_db)):
    # 调用service中登录方法，获取到用户信息
    user = user_service.login_user(db, user.username, user.password)

    # 封装生成token需要的用户信息
    user_info = {
        "sub": str(user.id),
        "username": user.username
    }
    token = create_access_token(user_info)

    data = {
        "access_token": token,
        "token_type": "Bearer"
    }
    return ResultModel(message="登录成功", data=data)


# 获取当前用户信息
@router.get("/profile", response_model=ResultModel[UserResponse])
async def profile(
        current_user  = Depends(get_current_user)
    ):
    return ResultModel(data=current_user )


# 查询用户信息(统一返回结果)
@router.get(
    "/{user_id}",
    response_model=ResultModel
)
async def get_user(user_id: int):
    result = user_service.get_user_byid(user_id)
    return ResultModel(data=result)