"""
Методы для обращения в БД в таблицу users
"""

from app.base_dao.base import BaseDao
from app.users.models import Users


class UsersDAO(BaseDao):
    model = Users
