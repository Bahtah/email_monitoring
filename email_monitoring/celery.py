from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_monitoring.settings")
app = Celery("email_monitoring")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'my_periodic_task': {
        'task': 'read_email.tasks.read_gmail_task_v2',
        'schedule': timedelta(seconds=15),
    },
}
