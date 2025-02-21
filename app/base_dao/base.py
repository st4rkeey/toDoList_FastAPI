"""
Набор универсальных запросов к БД (SQLAlchemy)
"""

from app.database import async_session_maker
from sqlalchemy import select, insert


class BaseDao:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """Общий метод для нахождения искомого значения по заданным фильтрам. Возвращает одну запись или None(Null)"""

        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        """Общий метод для добавления записей в таблицу"""

        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_all(cls, **filter_by):
        """Общий метод поиска одного или нескольких значений по заданным фильтрам"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
