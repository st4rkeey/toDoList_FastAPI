"""
Фоновые задачи Celery
"""

from celery import Celery
from app.config import (
    SMTP_HOST,
    SMTP_PASS,
    SMTP_PORT,
    SMTP_USER,
    REDIS_HOST,
    REDIS_PORT,
)
import smtplib


celery_app = Celery("tasks", broker=f"redis://{REDIS_HOST}:{REDIS_PORT}")


@celery_app.task
def send_email_task_created(email_to: str, username: str):
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(
            from_addr=SMTP_USER,
            to_addrs=email_to,
            msg=f"Hello {username}! You have created a new task",
        )
