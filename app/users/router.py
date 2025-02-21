"""
Роутер для пользователей
"""
from fastapi import APIRouter, Response

from app.exceptions import UserAlreadyExistException, IncorrectEmailOrPasswordException
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.schemas import SUserRegister, SUserLogin
from app.users.users_dao import UsersDAO

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    """Создание (Регистрация) нового юзера"""

    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(
        name=user_data.name, email=user_data.email, hashed_password=hashed_password
    )


@router.post("/login")
async def login_user(user_data: SUserLogin, response: Response):
    """EndPoint для входа пользователя по почте и паролю"""

    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return access_token
