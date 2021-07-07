import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw13_celery_parsing.settings')

app = Celery('hw13_celery_parsing')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # executes every odd hour
    'parsing-task-odd-hour': {
        'task': 'parsing_app.tasks.parsing_html',
        'schedule': crontab(minute=0, hour='1-23/2')
    }
}
