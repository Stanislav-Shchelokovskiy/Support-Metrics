import os
from typing import Callable

from celery import Celery
from celery.schedules import crontab
from celery.signals import worker_ready

import tasks.customers_activity_tasks as customers_activity
from configs.customers_activity_tasks_config import CustomersActivityTasksConfig


app = Celery(
    __name__,
    broker=os.environ['CELERY_BROKER_URL'],
    backend=os.environ['CELERY_RESULT_BACKEND'],
)


@worker_ready.connect
def on_startup(sender, **kwargs):
    tasks = [
        'customers_activity_load_tickets_types',
        'customers_activity_load_license_statuses',
        'customers_activity_load_conversion_statuses',
        'update_customers_activity',
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
    # update posts by clients every day at 4am
    sender.add_periodic_task(
        crontab(
            minute=0,
            hour=3,
        ),
        update_customers_activity.s(),
    )


@app.task(name='update_customers_activity')
def update_customers_activity(**kwargs):
    app.send_task(name='customers_activity_load_tags')
    app.send_task(name='customers_activity_load_groups')
    app.send_task(name='customers_activity_load_replies_types')
    app.send_task(name='customers_activity_load_components_features')
    app.send_task(name='customers_activity_load_platforms_products')
    app.send_task(name='customers_activity_load_tickets_with_licenses')
    app.send_task(name='customers_activity_load_employees_iterations')


@app.task(name='customers_activity_load_tags', bind=True)
def customers_activity_load_tags(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tags,
    )


@app.task(name='customers_activity_load_groups', bind=True)
def customers_activity_load_groups(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_groups,
    )


@app.task(name='customers_activity_load_replies_types', bind=True)
def customers_activity_load_replies_types(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_replies_types,
    )


@app.task(name='customers_activity_load_components_features', bind=True)
def customers_activity_load_components_features(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_components_features,
    )


@app.task(name='customers_activity_load_platforms_products', bind=True)
def customers_activity_load_platforms_products(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_platforms_products,
    )


@app.task(name='customers_activity_load_tickets_with_licenses', bind=True)
def customers_activity_load_tickets_with_licenses(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tickets_with_licenses,
        **CustomersActivityTasksConfig.get_tickets_with_licenses_period(),
    )


@app.task(name='customers_activity_load_tickets_types', bind=True)
def customers_activity_load_tickets_types(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tickets_types,
    )


@app.task(name='customers_activity_load_license_statuses', bind=True)
def customers_activity_load_license_statuses(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_license_statuses,
    )


@app.task(name='customers_activity_load_conversion_statuses', bind=True)
def customers_activity_load_conversion_statuses(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_conversion_statuses,
    )


@app.task(name='customers_activity_load_employees_iterations', bind=True)
def customers_activity_load_employees_iterations(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_employees_iterations,
        **CustomersActivityTasksConfig.get_tickets_with_licenses_period(),
    )


def run_retriable_task(task_instance, task: Callable, *args, **kwargs) -> str:
    try:
        return task(*args, **kwargs)
    except Exception as e:
        raise task_instance.retry(exc=e, countdown=600, max_retries=10)
