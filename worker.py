import os
from typing import Callable

from celery import Celery, chord
from celery.schedules import crontab
from celery.signals import worker_ready

import tasks.customers_activity_tasks as customers_activity
from configs.customers_activity_config import CustomersActivityConfig


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
        'customers_activity_load_tribes',
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
    chord(
        [
            customers_activity_load_tags.si(),
            customers_activity_load_groups.si(),
            customers_activity_load_tracked_groups.si(),
            customers_activity_load_replies_types.si(),
            customers_activity_load_components_features.si(),
            customers_activity_load_platforms_products.si(),
            customers_activity_load_customers_tickets.si(),
            customers_activity_load_employees_iterations.si(),
        ]
    )(customers_activity_build_tables.si())


@app.task(name='customers_activity_load_tickets_types', bind=True)
def customers_activity_load_tickets_types(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tickets_types,
    )

@app.task(name='customers_activity_load_tribes', bind=True)
def customers_activity_load_tribes(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tribes(),
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


@app.task(name='customers_activity_load_tracked_groups', bind=True)
def customers_activity_load_tracked_groups(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tracked_groups,
        start_date=CustomersActivityConfig.get_tickets_period()['start_date'],
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


@app.task(name='customers_activity_load_customers_tickets', bind=True)
def customers_activity_load_customers_tickets(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_customers_tickets,
        **CustomersActivityConfig.get_tickets_period(),
    )


@app.task(name='customers_activity_load_employees_iterations', bind=True)
def customers_activity_load_employees_iterations(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_employees_iterations,
        **CustomersActivityConfig.get_tickets_period(),
    )


@app.task(name='customers_activity_build_tables', bind=True)
def customers_activity_build_tables(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.build_tables,
        rank_period_offset=CustomersActivityConfig.get_rank_period_offset(),
    )


def run_retriable_task(task_instance, task: Callable, *args, **kwargs) -> str:
    try:
        return task(*args, **kwargs)
    except Exception as e:
        raise task_instance.retry(exc=e, countdown=600, max_retries=10)
