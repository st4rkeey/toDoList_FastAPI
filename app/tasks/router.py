"""
Роутер для задач
"""

from fastapi import APIRouter, Depends

from app.tasks.schemas import SCreateTask
from app.tasks.tasks_dao import TasksDao
from app.users.models import Users
from app.users.dependencies import get_current_user
from app.celery_tasks import send_email_task_created


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get("/")
async def get_tasks(user: Users = Depends(get_current_user)):
    """Метод для получения всех задач текущего пользователя"""

    return await TasksDao.find_all(user_id=user.id)


@router.post("/")
async def create_task(task_info: SCreateTask, user: Users = Depends(get_current_user)):
    """Метод для создания задачи для текущего пользователя"""

    await TasksDao.add(
        task_name=task_info.name,
        description=task_info.description,
        state=task_info.state,
        user_id=user.id,
    )
    try:
        send_email_task_created.delay(email_to=user.email, username=user.name)
    except Exception as e:
        print(e)
    return {
        "status": "200",
        "msg": "Your task has been created.",
    }
