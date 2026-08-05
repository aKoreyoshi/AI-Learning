"""
   :author: Kairos
   :description: 认证相关异常类
   :version: 1.0
   :date: 2026年08月05日,20:06:20
 """

from exceptions.business_exception import BusinessException

class TokenInvalidException(BusinessException):

    def __init__(self):
        super().__init__(code=40001, message="Token无效")


class TokenDataErrorException(BusinessException):

    def __init__(self):
        super().__init__(code=40002, message="Token数据错误")
