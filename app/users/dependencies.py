"""
Зависимости
"""

from datetime import datetime

from fastapi import Request, Depends
from jose import jwt, JWTError

from app.config import KEY, ALGORITHM
from app.exceptions import (
    TokenExpiredException,
    TokenAbsentException,
    IncorrectTokenFormatException,
    UserIsNotPresentException,
)
from app.users.users_dao import UsersDAO


def get_token(request: Request):
    """Функция получает токен из cookies, если нет - ошибка"""

    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    """Функция возвращает текущего пользователя, который вошел в свою учетную запись, если все условия соблюдены"""

    try:
        payload = jwt.decode(
            token,
            KEY,
            ALGORITHM,
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user
