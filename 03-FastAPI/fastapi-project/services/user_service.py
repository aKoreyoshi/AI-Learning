"""
   :author: Kairos
   :description: 关于用户业务的具体逻辑
   :version: 1.0
   :date: 2026年07月28日,18:44:44
 """

from schemas.user import UserCreate

# 由于目前暂未连接数据库，所以这里使用内存中的列表存储用户数据
users = []

# 用户注册
def register_user(user: UserCreate):

    # TODO 后续完善判断用户名唯一的逻辑

    new_user = {
        "id": len(users) + 1,
        "username": user.username,
        "password": user.password
    }
    users.append(new_user)

    return new_user

