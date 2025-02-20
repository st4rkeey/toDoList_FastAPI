"""
Файл с исключениями
"""

from fastapi import HTTPException, status


class TasksException(HTTPException):
    """Общий класс для HTTP ошибок"""

    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistException(TasksException):
    """Ошибка - Пользователь с такими данными уже существует"""

    status_code = status.HTTP_409_CONFLICT
    detail = "User with this username already exists."


class UserExistWithTheSameNameOrEmailException(TasksException):
    """Ошибка при обновлении данных о пользователи - Пользователь с такими данными уже существует"""

    status_code = status.HTTP_409_CONFLICT
    detail = "Such name or email already exists."


class IncorrectEmailOrPasswordException(TasksException):
    """Ошибка - неверный email или пароль"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password. Probably you are not registered"


class TokenExpiredException(TasksException):
    """Ошибка - JWT-token просрочен"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired."


class TokenAbsentException(TasksException):
    """Ошибка - токен отсутствует"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token absent."


class IncorrectTokenFormatException(TasksException):
    """Неверный формат JWT токена"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format."


class UserIsNotPresentException(TasksException):
    """Ошибка - нет пользователя с таким ID"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "user id is missing"
