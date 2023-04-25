import os
import hashlib
import help.index as help_index
import repository.server_repository as server_repository
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from collections.abc import Coroutine

from toolbox.utils.converters import JSON_to_object
from server_cache import ServerCache
from server_models import (
    TicketsWithIterationsParams,
    TentsParams,
    FeatureParams,
    StatAppState,
    ConversionStatusParams,
    EmployeeParams,
    CustomersParams,
)


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


async def get_repsonse_async(task: Coroutine):
    return get_response(json_data=await task)


# yapf: disable
@app.get('/get_tickets_with_iterations_period')
async def customers_activity_get_tickets_with_iterations_period():
    return await get_repsonse_async(
        server_repository.customers_activity_get_tickets_with_iterations_period()
    )


@app.get('/get_customers_groups')
async def customers_activity_get_customers_groups(tracked: bool = False):
    return await get_repsonse_async(
        server_repository.customers_activity_get_tracked_customers_groups()
        if tracked else
        server_repository.customers_activity_get_customers_groups()
    )


@app.get('/get_tickets_types')
async def customers_activity_get_tickets_types():
    return await get_repsonse_async(
        server_repository.customers_activity_get_tickets_types()
    )


@app.get('/get_frameworks')
async def customers_activity_get_frameworks():
    return await get_repsonse_async(
        server_repository.customers_activity_get_frameworks()
    )


@app.get('/get_operating_systems')
async def customers_activity_get_operating_systems():
    return await get_repsonse_async(
        server_repository.customers_activity_get_operating_systems()
    )


@app.get('/get_builds')
async def customers_activity_get_builds():
    return await get_repsonse_async(
        server_repository.customers_activity_get_builds()
    )


@app.get('/get_severity_values')
async def customers_activity_get_severity_values():
    return await get_repsonse_async(
        server_repository.customers_activity_get_severity_values()
    )


@app.get('/get_ticket_statuses')
async def customers_activity_get_ticket_statuses():
    return await get_repsonse_async(
        server_repository.customers_activity_get_ticket_statuses()
    )


@app.get('/get_ides')
async def customers_activity_get_ides():
    return await get_repsonse_async(
        server_repository.customers_activity_get_ides()
    )


@app.get('/get_tickets_tags')
async def customers_activity_get_tickets_tags():
    return await get_repsonse_async(
        server_repository.customers_activity_get_tickets_tags()
    )


@app.get('/get_replies_types')
async def customers_activity_get_cat_get_replies_types():
    return await get_repsonse_async(
        server_repository.customers_activity_get_replies_types()
    )


@app.post('/get_components')
async def customers_activity_get_cat_components(params: TentsParams):
    return await get_repsonse_async(
        server_repository.customers_activity_get_components(
            tent_ids=params.tents,
        )
    )


@app.post('/get_features')
async def customers_activity_get_cat_features(params: FeatureParams):
    return await get_repsonse_async(
        server_repository.customers_activity_get_features(
            tent_ids=params.tents,
            component_ids=params.components,
        )
    )


@app.post('/get_platforms')
async def customers_activity_get_platforms(params: TentsParams):
    return await get_repsonse_async(
        server_repository.customers_activity_get_platforms(
            tent_ids=params.tents,
        )
    )


@app.post('/get_products')
async def customers_activity_get_products(params: TentsParams):
    return await get_repsonse_async(
        server_repository.customers_activity_get_products(
            tent_ids=params.tents,
        )
    )


@app.get('/get_group_by_periods')
async def customers_activity_get_group_by_periods():
    return await get_repsonse_async(
        server_repository.customers_activity_get_group_by_periods()
    )


# yapf: enable
@app.get('/get_periods_array')
async def customers_activity_get_periods_array(
    start: str,
    end: str,
    format: str,
):
    return await get_repsonse_async(
        server_repository.customers_activity_get_periods_array(
            start=start,
            end=end,
            format=format,
        )
    )


@app.get('/get_license_statuses')
async def customers_activity_get_license_statuses():
    return await get_repsonse_async(
        server_repository.customers_activity_get_license_statuses()
    )


@app.post('/get_conversion_statuses')
async def customers_activity_get_conversion_statuses(
    params: ConversionStatusParams
):
    return await get_repsonse_async(
        server_repository.customers_activity_get_conversion_statuses(
            license_status_ids=params.license_statuses
        )
    )


@app.get('/get_positions')
async def customers_activity_get_emp_positions():
    return await get_repsonse_async(
        server_repository.customers_activity_get_emp_positions()
    )


@app.get('/get_emp_tribes')
async def customers_activity_get_emp_tribes():
    return await get_repsonse_async(
        server_repository.customers_activity_get_emp_tribes()
    )


@app.get('/get_emp_tents')
async def customers_activity_get_emp_tents():
    return await get_repsonse_async(
        server_repository.customers_activity_get_emp_tents()
    )


@app.post('/get_employees')
async def customers_activity_get_employees(params: EmployeeParams):
    return await get_repsonse_async(
        server_repository.customers_activity_get_employees(
            position_ids=params.positions,
            tribe_ids=params.tribes,
            tent_ids=params.tents,
        )
    )


@app.post('/get_customers')
async def customers_activity_get_customers(
    params: CustomersParams,
    search: str = '',
    skip: int = 0,
    take: int = 0,
):
    return await get_repsonse_async(
        server_repository.customers_activity_get_customers(
            filter_values=params.customers,
            search=search,
            skip=skip,
            take=take,
        )
    )


@app.post('/validate_customers')
async def customers_activity_validate_customers(params: CustomersParams):
    return await get_repsonse_async(
        server_repository.customers_activity_validate_customers(
            values=params.customers
        )
    )


@app.post('/get_tickets_with_iterations_aggregates')
async def customers_activity_get_tickets_with_iterations_aggregates(
    group_by_period: str,
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
):
    return await get_repsonse_async(
        server_repository.
        customers_activity_get_tickets_with_iterations_aggregates(
            group_by_period=group_by_period,
            range_start=range_start,
            range_end=range_end,
            use_baseline_aligned_mode=baseline_aligned_mode_enabled,
            **body.get_field_values(),
        )
    )


@app.post('/get_tickets_with_iterations_raw')
async def customers_activity_get_tickets_with_iterations_raw(
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
):
    return await get_repsonse_async(
        server_repository.customers_activity_get_tickets_with_iterations_raw(
            range_start=range_start,
            range_end=range_end,
            use_baseline_aligned_mode=baseline_aligned_mode_enabled,
            **body.get_field_values(),
        )
    )


@app.post('/get_customers_activity_display_filter')
async def get_customers_activity_display_filter(
    body: TicketsWithIterationsParams
):
    return await get_repsonse_async(
        server_repository.customers_activity_get_display_filter(body)
    )


@app.get('/get_customers_activity_help')
async def get_customers_activity_help():
    return await get_repsonse_async(
        help_index.get_customers_activity_descriptions()
    )


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
