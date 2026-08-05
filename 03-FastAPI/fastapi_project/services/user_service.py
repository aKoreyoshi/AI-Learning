"""
   :author: Kairos
   :description: 关于用户业务的具体逻辑
   :version: 1.0
   :date: 2026年07月28日,18:44:44
 """

from fastapi import HTTPException
from schemas.user import UserCreate, UserLogin
from exceptions.user_exception import (UserNotFoundException, UsernameExistException,
                                       UsernameIsNoneException, UsernameOrPasswordErrorException)
from crud.user import get_user_by_username, create_user
from sqlalchemy.orm import Session
from models.user import User
from utils.password import verify_password

# 由于目前暂未连接数据库，所以这里使用内存中的列表存储用户数据
users = []

# 用户注册
def register_user(db: Session, username: str, password: str):

    # 用户名不能为空
    if username is None:
        raise UsernameIsNoneException()

    # 判断用户名是否已存在
    user = get_user_by_username(db, username)
    if user:
        raise UsernameExistException()

    # 调用CRUD方法，添加用户
    new_user = create_user(db, username, password)

    return new_user


# 用户登录
def login_user(db: Session, username: str, password: str):

    # 首先判断用户是否存在
    user = get_user_by_username(db, username)
    if user is None:
        # 用户不存在，直接抛出“用户找不到异常”
        raise UserNotFoundException()

    # 用户存在，判断密码是否正确
    flag = verify_password(password, user.password)
    if not flag:
        # 密码错误则抛出异常
        raise UsernameOrPasswordErrorException()

    return user

# 查询用户 根据用户id
def get_user_byid(user_id: int):
    for item in users:
        if item["id"] == user_id:
            return item

    # 用户如果不存在，直接抛出异常
    raise UserNotFoundException()

