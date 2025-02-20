"""
Модель таблицы users (SQLAlchemy)
"""

from sqlalchemy import Column, Integer, String

from app.database import Base


class Users(Base):
    """Модель таблицы users"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
