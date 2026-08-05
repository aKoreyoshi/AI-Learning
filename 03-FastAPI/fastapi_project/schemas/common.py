"""
   :author: Kairos
   :description: 创建统一返回体模型结构
   :version: 1.0
   :date: 2026年07月31日,00:19:51
 """

from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ResultModel(BaseModel, Generic[T]):
    """
    统一返回体模型结构
    """
    code: int = 200
    message: str = "success"
    data: T | None = None
