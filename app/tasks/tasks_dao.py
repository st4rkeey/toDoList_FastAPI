"""
Методы для обращения в БД в таблицу tasks
"""

from app.base_dao.base import BaseDao
from app.tasks.models import Tasks


class TasksDao(BaseDao):
    model = Tasks
