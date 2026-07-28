"""
   :author: Kairos
   :description: fastAPI 的异常处理
   :version: 1.0
   :date: 2026年07月28日,23:50:48
 """

from fastapi import HTTPException

def http_exception():
    raise HTTPException(
        status_code=402,
        detail="Not Found"
    )

http_exception()
