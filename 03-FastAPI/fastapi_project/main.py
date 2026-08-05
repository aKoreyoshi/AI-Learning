"""
   :author: Kairos
   :description: 程序主入口
   :version: 1.0
   :date: 2026年07月28日,18:07:46
 """

from fastapi import FastAPI
from starlette.responses import JSONResponse

from routers import user
from exceptions.business_exception import BusinessException

app = FastAPI(
    title="User Management API",
    version="1.0.0"
)

# 添加全局异常处理
@app.exception_handler(BusinessException)
async def business_exception_handler(
        request,
        exc
    ):
    return JSONResponse(
        status_code=400,
        content={
            "code": exc.code,
            "message": exc.message,
            "data": None
        }
    )

# 将路由注册到app中
app.include_router(
    user.router
)

@app.get("/")
async def root():
    return {
        "message": "FastAPI is running..."
    }
