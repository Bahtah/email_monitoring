from celery import shared_task


@shared_task
def read_gmail_task_v2():
    from read_email.email_parser import read_gmail
    num_unread_messages = read_gmail()
    return f"Найдено {num_unread_messages} непрочитанных сообщений"