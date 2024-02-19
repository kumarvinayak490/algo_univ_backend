# tasks.py
import os
import subprocess
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')


app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def execute_code(code):
    try:
        result = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT,
                                         timeout=10, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output
    except subprocess.TimeoutExpired:
        return "Execution timed out."
    except Exception as e:
        return str(e)
