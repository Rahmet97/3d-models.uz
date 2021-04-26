import os  
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_3d.settings')
celery_app = Celery('model_3d')  
celery_app.config_from_object('django.conf:settings', namespace='CELERY')  
celery_app.autodiscover_tasks()