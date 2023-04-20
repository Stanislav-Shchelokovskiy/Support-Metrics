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
        'customers_activity_load_tents',
        'customers_activity_load_operating_systems',
        'customers_activity_load_frameworks',
        'customers_activity_load_severity_values',
        'customers_activity_load_ticket_statuses',
        'customers_activity_load_replies_types',
        'customers_activity_load_platforms_products',
        'customers_activity_load_ides',
        'customers_activity_load_employees',
    ]
    if int(os.environ['UPDATE_CUSTOMERS_ACTIVITY_ON_STARTUP']):
        tasks.append('update_customers_activity')

    sender_app: Celery = sender.app
    with sender_app.connection() as conn:
        for task in tasks:
            sender_app.send_task(
                name=task,
                connection=conn,
            )


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(
            minute=0,
            hour=1,
            day_of_week=(1, 3, 5),
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
            customers_activity_load_builds.si(),
            customers_activity_load_components_features.si(),
            customers_activity_load_customers_tickets.si(),
            customers_activity_load_employees_iterations.si(),
        ]
    )(customers_activity_process_staged_data.si())


@app.task(name='customers_activity_load_tickets_types', bind=True)
def customers_activity_load_tickets_types(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tickets_types,
    )


@app.task(name='customers_activity_load_frameworks', bind=True)
def customers_activity_load_frameworks(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_frameworks,
    )


@app.task(name='customers_activity_load_operating_systems', bind=True)
def customers_activity_load_operating_systems(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_operating_systems,
    )


@app.task(name='customers_activity_load_builds', bind=True)
def customers_activity_load_builds(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_builds,
    )


@app.task(name='customers_activity_load_severity_values', bind=True)
def customers_activity_load_severity_values(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_severity_values,
    )


@app.task(name='customers_activity_load_ticket_statuses', bind=True)
def customers_activity_load_ticket_statuses(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_ticket_statuses,
    )


@app.task(name='customers_activity_load_ides', bind=True)
def customers_activity_load_ides(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_ides,
    )


@app.task(name='customers_activity_load_tribes', bind=True)
def customers_activity_load_tribes(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tribes,
    )


@app.task(name='customers_activity_load_tents', bind=True)
def customers_activity_load_tents(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_tents,
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
        end_date='9999-12-31',
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


@app.task(name='customers_activity_load_employees', bind=True)
def customers_activity_load_employees(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.load_employees,
        start_date=CustomersActivityConfig.get_tickets_period()['start_date'],
    )


@app.task(name='customers_activity_process_staged_data', bind=True)
def customers_activity_process_staged_data(self, **kwargs):
    return run_retriable_task(
        self,
        customers_activity.process_staged_data,
        rank_period_offset=CustomersActivityConfig.get_rank_period_offset(),
    )


def run_retriable_task(task_instance, task: Callable, *args, **kwargs) -> str:
    try:
        return task(*args, **kwargs)
    except Exception as e:
        raise task_instance.retry(exc=e, countdown=600, max_retries=10)
