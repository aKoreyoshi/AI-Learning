"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年08月05日,15:42:05
 """

from database.database import Base,engine
from models import user

Base.metadata.create_all(bind=engine)