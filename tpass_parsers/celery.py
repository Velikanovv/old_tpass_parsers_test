import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tpass_parsers.settings')

app = Celery('tpass_parsers')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'Проверка пропусков всех машин [17:00]': {
        'task': 'companies.tasks.parse_pass_all',
        'schedule': crontab(hour=18, minute=35)
    },
}

app.autodiscover_tasks()
