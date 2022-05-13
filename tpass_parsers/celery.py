import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tpass_parsers.settings')

app = Celery('tpass_parsers')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'Проверка штрафов новых авто [Ежеминутно]': {
        'task': 'companies.tasks.parse_fines_new',
        'schedule': crontab(minute='*/1')
    },
    'Проверка пропусков новых авто [Ежеминутно]': {
        'task': 'companies.tasks.parse_pass_new',
        'schedule': crontab(minute='*/1')
    },
    'Проверка пропусков всех машин [17:00]': {
        'task': 'companies.tasks.parse_pass_all',
        'schedule': crontab(hour=17, minute=00)
    },
    'Проверка штрафов всех машин [00:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=0, minute=0)
    },
    'Проверка штрафов всех машин [04:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=4, minute=0)
    },
    'Проверка штрафов всех машин [08:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=8, minute=0)
    },
    'Проверка штрафов всех машин [10:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=10, minute=0)
    },
    'Проверка штрафов всех машин [12:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=12, minute=0)
    },
    'Проверка штрафов всех машин [14:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=14, minute=0)
    },
    'Проверка штрафов всех машин [16:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=16, minute=0)
    } ,
    'Проверка штрафов всех машин [18:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=18, minute=0)
    } ,
    'Проверка штрафов всех машин [20:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=20, minute=0)
    } ,
    'Проверка штрафов всех машин [22:00]': {
        'task': 'companies.tasks.parse_fines_all',
        'schedule': crontab(hour=22, minute=0)
    } ,
}

app.autodiscover_tasks()
