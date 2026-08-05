"""
   :author: Kairos
   :description: 数据库负责的映射表
   :version: 1.0
   :date: 2026年08月05日,15:34:54
 """

from sqlalchemy import Column, Integer, String
from database.database import Base

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(50), unique=True, nullable=False, index=True)

    password = Column(String(255), nullable=False)

