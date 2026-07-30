"""
   :author: Kairos
   :description: 依赖模块 (依赖注入)
   :version: 1.0
   :date: 2026年07月30日,16:59:26
 """
from fastapi import Header, HTTPException, Depends
import security
from services import user_service


# 获取当前用户token
def get_token(
        authorization: str = Header(alias="Authorization")
    ):
    return authorization


# 获取当前用户
def get_current_user(
        token = Depends(get_token)
    ):
    payload = security.decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="无效的token"
        )
    user = user_service.get_user_byid(payload["user_id"])

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="用户不存在"
        )
    return user