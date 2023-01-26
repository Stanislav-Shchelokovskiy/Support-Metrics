import os
import hashlib
import json
import repository.server_repository as server_repository
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from toolbox.utils.converters import JSON_to_object
from server_cache import ServerCache
from server_models import (
    TicketsWithIterationsParams,
    TribeParams,
    FeatureParams,
    ProductParams,
    StatAppState,
    ConversionStatusParams,
    EmployeeParams,
    CustomersParams,
)
from help.index import Index as help_index


server_cache = ServerCache()

app = FastAPI()

origins = JSON_to_object.convert(os.environ['CORS_ORIGINS'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


def get_response(json_data: str) -> Response:
    return Response(
        content=json_data,
        media_type='application/json',
    )


@app.get('/get_tickets_with_iterations_period')
def customers_activity_get_tickets_with_iterations_period():
    # yapf: disable
    df_json = server_repository.customers_activity_get_tickets_with_iterations_period()
    # yapf: enable
    return get_response(json_data=df_json)


@app.get('/get_customers_groups')
def customers_activity_get_customers_groups(tracked: bool = False):
    df_json = (
        server_repository.customers_activity_get_tracked_customers_groups()
        if tracked else
        server_repository.customers_activity_get_customers_groups()
    )
    return get_response(json_data=df_json)


@app.get('/get_tickets_types')
def customers_activity_get_tickets_types():
    df_json = server_repository.customers_activity_get_tickets_types()
    return get_response(json_data=df_json)


@app.get('/get_tickets_tags')
def customers_activity_get_tickets_tags():
    df_json = server_repository.customers_activity_get_tickets_tags()
    return get_response(json_data=df_json)


@app.get('/get_replies_types')
def customers_activity_get_cat_get_replies_types():
    df_json = server_repository.customers_activity_get_replies_types()
    return get_response(json_data=df_json)


@app.post('/get_components')
def customers_activity_get_cat_components(params: TribeParams):
    df_json = server_repository.customers_activity_get_components(
        tribe_ids=params.tribes,
    )
    return get_response(json_data=df_json)


@app.post('/get_features')
def customers_activity_get_cat_features(params: FeatureParams):
    df_json = server_repository.customers_activity_get_features(
        tribe_ids=params.tribes,
        component_ids=params.components,
    )
    return get_response(json_data=df_json)


@app.post('/get_platforms')
def customers_activity_get_platforms(params: TribeParams):
    df_json = server_repository.customers_activity_get_platforms(
        tribe_ids=params.tribes,
    )
    return get_response(json_data=df_json)


@app.post('/get_products')
def customers_activity_get_products(params: ProductParams):
    df_json = server_repository.customers_activity_get_products(
        tribe_ids=params.tribes,
        platform_ids=params.platforms,
    )
    return get_response(json_data=df_json)


@app.get('/get_group_by_periods')
def customers_activity_get_group_by_periods():
    return get_response(
        json_data=server_repository.customers_activity_get_group_by_periods()
    )


@app.get('/get_license_statuses')
def customers_activity_get_license_statuses():
    return get_response(
        json_data=server_repository.customers_activity_get_license_statuses()
    )


@app.post('/get_conversion_statuses')
def customers_activity_get_conversion_statuses(params: ConversionStatusParams):
    return get_response(
        json_data=server_repository.customers_activity_get_conversion_statuses(
            license_status_ids=params.license_statuses
        )
    )


@app.get('/get_positions')
def customers_activity_get_emp_positions():
    return get_response(
        json_data=server_repository.customers_activity_get_emp_positions()
    )


@app.get('/get_emp_tribes')
def customers_activity_get_emp_tribes():
    return get_response(
        json_data=server_repository.customers_activity_get_emp_tribes()
    )


@app.post('/get_employees')
def customers_activity_get_employees(params: EmployeeParams):
    return get_response(
        json_data=server_repository.customers_activity_get_employees(
            position_ids=params.positions,
            tribe_ids=params.tribes,
        )
    )


@app.post('/get_customers')
def customers_activity_get_customers(
    params: CustomersParams,
    search: str = '',
    skip: int = 0,
    take: int = 0,
):
    return get_response(
        json_data=server_repository.customers_activity_get_customers(
            filter_values=params.customers,
            search=search,
            skip=skip,
            take=take,
        )
    )


@app.post('/validate_customers')
def customers_activity_validate_customers(params: CustomersParams):
    return get_response(
        json_data=server_repository.customers_activity_validate_customers(
            values=params.customers
        )
    )


@app.post('/get_tickets_with_iterations_aggregates')
def customers_activity_get_tickets_with_iterations_aggregates(
    group_by_period: str,
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
):
    df_json = server_repository.customers_activity_get_tickets_with_iterations_aggregates(
        group_by_period=group_by_period,
        range_start=range_start,
        range_end=range_end,
        use_baseline_aligned_mode=baseline_aligned_mode_enabled,
        **body.__dict__,
    )
    return get_response(json_data=df_json)


@app.post('/get_tickets_with_iterations_raw')
def customers_activity_get_tickets_with_iterations_raw(
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
):
    df_json = server_repository.customers_activity_get_tickets_with_iterations_raw(
        range_start=range_start,
        range_end=range_end,
        use_baseline_aligned_mode=baseline_aligned_mode_enabled,
        **body.__dict__,
    )
    return get_response(json_data=df_json)


@app.post('/push_state')
def push_state(params: StatAppState):
    state = params.state
    state_id = hashlib.md5(state.encode()).hexdigest()
    server_cache.stat_app_state.save(value=state, key=[state_id])
    return get_response(json_data=state_id)


@app.get('/pull_state')
def pull_state(state_id: str, ):
    state = server_cache.stat_app_state.get(state_id)
    return get_response(json_data=state)


@app.get('/get_customers_activity_help')
def get_customers_activity_help():
    return get_response(
        json_data=json.dumps(help_index.get_customers_activity_descriptions())
    )


@app.post('/get_customers_activity_display_filter')
def get_customers_activity_display_filter(body: TicketsWithIterationsParams):
    filters = server_repository.customers_activity_get_display_filter(
        aliases={k: v.alias for k, v in body.__fields__.items()},
        **body.__dict__,
    )
    return get_response(json_data=json.dumps(filters))
