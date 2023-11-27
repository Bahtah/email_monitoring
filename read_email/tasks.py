
from celery import shared_task
from .email_parser2 import process_and_save_emails


@shared_task
def process_and_save_emails_task():
    return process_and_save_emails()
