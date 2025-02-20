"""
Схемы для задач
"""

from pydantic import BaseModel
from enum import Enum


class CEnum(Enum):
    """Схема для выбора определенных значений при изменении статуса задачи"""

    VALUE_1 = "New"
    VALUE_2 = "In process"
    VALUE_3 = "Finished"


class SCreateTask(BaseModel):
    """Схема валидации данных для добавления новой задачи"""

    name: str
    description: str
    state: str = "New"
