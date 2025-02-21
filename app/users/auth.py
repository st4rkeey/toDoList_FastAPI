"""
Файл для хранения методов, участвуюших в авторизации и аутентификации
"""

from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

from pydantic import EmailStr

from app.config import KEY, ALGORITHM
from app.users.users_dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Функция для кэширования пароля пользователя"""

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Функция для проверки соответствия пароля, введенного пользователем - паролю из БД"""

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """Функция создания токена"""

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, KEY, ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    """Функция для поиска зарегистрированного пользователя"""

    user = await UsersDAO.find_one_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
