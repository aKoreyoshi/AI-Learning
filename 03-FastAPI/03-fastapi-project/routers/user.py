"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,18:11:21
 """

from fastapi import APIRouter

# 创建一个路由
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_users():
    return {
        "message": "user list"
    }