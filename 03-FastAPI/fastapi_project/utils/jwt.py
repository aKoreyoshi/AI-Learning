"""
   :author: Kairos
   :description: JWT工具类
   :version: 1.0
   :date: 2026年08月05日,18:59:47
 """

from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

"""
    token实际组成部分：
    token - header.pyload.signature
"""

# secret key
SECRET_KEY = "your-secret-key"

# 加密算法
ALGORITHM = "HS256"

# token有效时间
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 随机生成一个JWT访问令牌
def create_access_token(data: dict):

    # 复制一份原数据，避免直接修改原始数据(防止副作用)
    to_encode = data.copy()

    # 计算token过期的时间
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # 将过期时间加入到to_encode中
    to_encode.update({"exp": expire})

    # 生成token
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


# 解析token
def decode_access_token(token: str):
    try:
        pyload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return pyload
    except JWTError as e:
        print(f"JWT解析失败：,{e}")
        return None