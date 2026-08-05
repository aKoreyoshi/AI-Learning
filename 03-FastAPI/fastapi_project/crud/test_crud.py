"""
   :author: Kairos
   :description: 测试连接数据库操作
   :version: 1.0
   :date: 2026年08月05日,16:19:15
 """

from database.database import SessionLocal
from crud.user import create_user

db = SessionLocal()

# 添加一条数据
user = create_user(db, "马聪", "123")

print(user.id)
print(user.username)

db.close()
