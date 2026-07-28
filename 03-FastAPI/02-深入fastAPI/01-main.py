"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,14:59:58
 """

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello mac"}
