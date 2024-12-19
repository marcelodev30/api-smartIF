from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartIF.settings')
app = Celery('smartIF')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    worker_pool='threads',  # Usa múltiplas threads
    worker_concurrency=5,   # Define o número de threads
)


app.conf.beat_schedule = {
    'verificar-e-executar-cenarios-a-cada-minuto': {
        'task': 'modulosSmart.tasks.verificar_e_executar_cenarios',
        'schedule': crontab(minute='*/1'), 
    },
}