"""
   :author: Kairos
   :description: 关于用户业务的具体逻辑
   :version: 1.0
   :date: 2026年07月28日,18:44:44
 """

from fastapi import HTTPException
from schemas.user import UserCreate, UserLogin
from exceptions.user_exception import UserNotFoundException, UsernameExistException

# 由于目前暂未连接数据库，所以这里使用内存中的列表存储用户数据
users = []

# 用户注册
def register_user(user: UserCreate):

    # 判断用户名是否已存在
    for item in users:
        if item["username"] == user.username:
            raise UsernameExistException()

    # 添加用户
    new_user = {
        "id": len(users) + 1,
        "username": user.username,
        "password": user.password
    }

    # 保存添加的用户信息
    users.append(new_user)

    return new_user


# 用户登录
def login_user(user: UserLogin):

    # 遍历用户列表，判断用户名是否存在
    for item in users:
        if item["username"] == user.username:
            # 判断密码是否正确
            if item["password"] == user.password:
                return user

            raise HTTPException(
                status_code=401,
                detail="用户名或密码错误"
            )

    raise HTTPException(
        status_code=401,
        detail="用户名或密码错误"
    )

# 查询用户 根据用户id
def get_user_byid(user_id: int):
    for item in users:
        if item["id"] == user_id:
            return item

    # 用户如果不存在，直接抛出异常
    raise UserNotFoundException()

