"""
   :author: Kairos
   :description: 密码加密工具类
   :version: 1.0
   :date: 2026年08月05日,17:44:43
 """

from passlib.context import CryptContext


# 创建密码处理器  使用bcrypt算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 密码加密
def hash_password(password: str):
    print(password)
    print(len(password.encode("utf-8")))
    return pwd_context.hash(password)


# 验证密码
def verify_password(plain_pwd: str, hashed_pwd: str):
    return pwd_context.verify(plain_pwd, hashed_pwd)


