import time
from celery import shared_task 
from celery import Celery

app = Celery()

@shared_task
def send_massage_email(recipient):
    print(recipient)
    print('start sleep')
    time.sleep(10)
    print('end sleep')
    return


@app.task
def add():
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
