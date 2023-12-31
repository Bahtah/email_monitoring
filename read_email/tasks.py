from celery import shared_task
from .reg2 import process_email


@shared_task
def read_gmail_task_v2():
    from read_email.reg2 import read_gmail
    num_unread_messages = read_gmail()
    return f"Найдено {num_unread_messages} непрочитанных сообщений"


@shared_task
def process_email_task_v2(email_data):
    return process_email(email_data)

