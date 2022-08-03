import os

from celery import Celery
from celery.schedules import crontab
from celery.signals import worker_ready

import tasks


app = Celery(
    __name__,
    broker=os.environ['CELERY_BROKER_URL'],
    backend=os.environ['CELERY_RESULT_BACKEND'],
)


@worker_ready.connect
def on_startup(sender, **kwargs):
    tasks = [
        'update_client_posts_by_tribes',
    ]
    sender_app: Celery = sender.app
    with sender_app.connection() as conn:
        for task in tasks:
            sender_app.send_task(
                name=task,
                connection=conn,
            )


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # update posts by clients every day at 5am
    sender.add_periodic_task(
        crontab(
            minute=0,
            hour=1,
        ),
        update_client_posts_by_tribes.s(),
    )


@app.task(name='update_client_posts_by_tribes')
def update_client_posts_by_tribes(**kwargs):
    tasks.update_client_posts_by_tribes()
