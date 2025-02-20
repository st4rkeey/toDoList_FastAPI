"""
Модель таблицы tasks (SQLAlchemy)
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Enum

from app.database import Base


class Tasks(Base):
    """Модель таблицы tasks"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    state = Column(Enum("New", "In process", "Finished"), nullable=False, default="New")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
