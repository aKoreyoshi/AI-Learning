"""
   :author: Kairos
   :description: 创建统一返回体模型结构
   :version: 1.0
   :date: 2026年07月31日,00:19:51
 """

from typing import Any
from pydantic import BaseModel

class ResultModel(BaseModel):
    """
    统一返回体模型结构
    """
    code: int = 200
    message: str = "success"
    data: Any = None
