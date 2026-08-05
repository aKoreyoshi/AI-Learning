"""
   :author: Kairos
   :description: 负责管理数据库连接
   :version: 1.0
   :date: 2026年08月05日,15:20:27
 """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = ("mysql+pymysql://root:macong@localhost:3306/fastapi_project")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# 创建数据库连接
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()