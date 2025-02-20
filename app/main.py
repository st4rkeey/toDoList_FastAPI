"""
Основной модуль приложения FastAPI
"""

from fastapi import FastAPI

from app.users.router import router as users_router
from app.tasks.router import router as tasks_router

app = FastAPI()

app.include_router(users_router)
app.include_router(tasks_router)


@app.get("/")
async def root():
    return {"message": "Healthy FastAPI"}
