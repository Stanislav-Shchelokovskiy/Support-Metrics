import os
from typing import Callable

from celery import Celery, chord, chain, group
from celery.schedules import crontab
from celery.signals import worker_ready

import tasks.tasks as tasks
import tasks.employees as employees
import configs.config as config


app = Celery(__name__)
app.conf.setdefault('broker_connection_retry_on_startup', True)


@worker_ready.connect
def on_startup(sender, **kwargs):
    tasks = [
        'load_tickets_types',
        'load_license_statuses',
        'load_conversion_statuses',
        'load_tribes',
        'load_tents',
        'load_operating_systems',
        'load_frameworks',
        'load_severity_values',
        'load_ticket_statuses',
        'load_replies_types',
        'load_platforms_products',
        'load_ides',
    ]
    if int(os.environ['UPDATE_ON_STARTUP']):
        tasks.append('update_support_metrics')
    else:
        tasks.append('load_employees'),
        tasks.append('load_csi'),

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
        update_support_metrics.s(),
    )


@app.task(name='update_support_metrics')
def update_support_metrics(**kwargs):
    chord(
        [
            load_tags.si(),
            load_groups.si(),
            load_tracked_groups.si(),
            load_builds.si(),
            load_components_features.si(),
            load_csi.si(),
            
            chain(
                get_employees.si(),
                group(
                    load_employees.s(),
                    load_employees_iterations.s(),
                )
            ),
            load_customers_tickets.si(),
        ]
    )(process_staged_data.si())


@app.task(name='load_tickets_types', bind=True)
def load_tickets_types(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_tickets_types,
    )


@app.task(name='load_frameworks', bind=True)
def load_frameworks(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_frameworks,
    )


@app.task(name='load_operating_systems', bind=True)
def load_operating_systems(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_operating_systems,
    )


@app.task(name='load_builds', bind=True)
def load_builds(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_builds,
    )


@app.task(name='load_severity_values', bind=True)
def load_severity_values(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_severity,
    )


@app.task(name='load_ticket_statuses', bind=True)
def load_ticket_statuses(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_ticket_statuses,
    )


@app.task(name='load_ides', bind=True)
def load_ides(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_ides,
    )


@app.task(name='load_tribes', bind=True)
def load_tribes(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_tribes,
    )


@app.task(name='load_tents', bind=True)
def load_tents(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_tents,
    )


@app.task(name='load_license_statuses', bind=True)
def load_license_statuses(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_license_statuses,
    )


@app.task(name='load_conversion_statuses', bind=True)
def load_conversion_statuses(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_conversion_statuses,
    )


@app.task(name='load_tags', bind=True)
def load_tags(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_tags,
    )


@app.task(name='load_groups', bind=True)
def load_groups(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_groups,
    )


@app.task(name='load_tracked_groups', bind=True)
def load_tracked_groups(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_tracked_groups,
        start_date=config.get_tickets_period()['start_date'],
        end_date='9999-12-31',
    )


@app.task(name='load_replies_types', bind=True)
def load_replies_types(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_replies_types,
    )


@app.task(name='load_components_features', bind=True)
def load_components_features(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_components_features,
    )


@app.task(name='load_platforms_products', bind=True)
def load_platforms_products(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_platforms_products,
    )


@app.task(name='load_customers_tickets', bind=True)
def load_customers_tickets(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_customers_tickets,
        **config.get_tickets_period(),
    )


@app.task(name='get_employees', bind=True)
def get_employees(self, **kwargs):
    return run_retriable_task(
        self,
        employees.get_employees,
    )


@app.task(name='load_employees', bind=True)
def load_employees(self, *args, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_employees,
        start_date=config.get_emp_start(),
        employees_json=args[0],
    )


@app.task(name='load_employees_iterations', bind=True)
def load_employees_iterations(self, *args, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_employees_iterations,
        **config.get_tickets_period(),
        employees_json=args[0],
    )


@app.task(name='load_csi', bind=True)
def load_csi(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.load_csi,
    )


@app.task(name='process_staged_data', bind=True)
def process_staged_data(self, **kwargs):
    return run_retriable_task(
        self,
        tasks.process_staged_data,
        rank_period_offset=config.get_rank_period_offset(),
        years_of_history=config.years_of_history(),
    )


def run_retriable_task(task_instance, task: Callable, *args, **kwargs) -> str:
    try:
        return task(*args, **kwargs)
    except Exception as e:
        raise task_instance.retry(exc=e, countdown=600, max_retries=10)
