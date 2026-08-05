"""
   :author: Kairos
   :description: 用户对数据库的操作
   :version: 1.0
   :date: 2026年08月05日,15:21:07
 """

from sqlalchemy.orm import Session
from models.user import User
from utils.password import hash_password

# 根据用户名查询用户
def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user


# 创建用户
def create_user(db: Session, username: str, password: str):

    user = User(
        username = username,
        # 密码加密
        password = hash_password(password)
    )

    db.add(user)
    db.commit()
    db.flush()
    return user