"""
   :author: Kairos
   :description: 依赖模块 (依赖注入)
   :version: 1.0
   :date: 2026年07月30日,16:59:26
 """
from fastapi import Header, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database.database import get_db
from utils.jwt import decode_access_token
from crud.user import get_user_by_username
from exceptions.auth_exception import TokenInvalidException, TokenDataErrorException
from exceptions.user_exception import UserNotFoundException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# 获取当前用户token
def get_token(
        authorization: str = Header(alias="Authorization")
    ):
    return authorization


# 获取当前用户
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
    ):
    print(f"========================token = {token}")
    # 解析token
    pyload = decode_access_token(token)
    print(f"========================pyload = {pyload}")
    # token无效
    if not pyload:
        raise TokenInvalidException()

    # 获取到用户名
    username = pyload.get("username")
    if not username:
        raise TokenDataErrorException()

    # 根据用户名拿到用户信息
    user = get_user_by_username(db, username)

    if not user:
        raise UserNotFoundException()
    # 返回用户信息
    return user