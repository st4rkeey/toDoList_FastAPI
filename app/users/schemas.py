"""
Схемы для пользователей
"""

from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    """Модель для валидации данных при регистрации пользователя"""

    name: str
    email: EmailStr
    password: str


class SUserLogin(BaseModel):
    """Модель для валидации данных при входе в учетную запись пользователя"""

    email: EmailStr
    password: str
