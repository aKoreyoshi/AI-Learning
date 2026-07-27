"""
   :author: Kairos
   :description:
   :version: 1.0
   :date: 2026年07月28日,00:31:56
 """


from fastapi import FastAPI

app = FastAPI()

print(type(app))
print(dir(app))
print(app.routes)