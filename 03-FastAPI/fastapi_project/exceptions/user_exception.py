"""
   :author: Kairos
   :description: 用户异常类
   :version: 1.0
   :date: 2026年07月30日,23:32:48
 """

from exceptions.business_exception import BusinessException

class UserNotFoundException(BusinessException):
    """
    用户不存在异常
    """
    def __init__(self):
        super().__init__(code=10001, message="用户不存在")


class UsernameExistException(BusinessException):
    """
    用户名已存在异常
    """
    def __init__(self):
        super().__init__(code=10002, message="用户名已存在")
