"""
   :author: Kairos
   :description: 通用异常类
   :version: 1.0
   :date: 2026年07月30日,23:46:15
 """

class BusinessException(Exception):

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(message)