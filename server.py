import os
import help.index as help_index
import repository.server_repository as server_repository
import toolbox.cache.view_state_cache as view_state_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from collections.abc import Coroutine

from toolbox.utils.converters import JSON_to_object
from server_models import (
    TicketsWithIterationsParams,
    TentsParams,
    FeatureParams,
    ViewState,
    ConversionStatusParams,
    EmployeeParams,
    CustomersParams,
)


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
@app.get('/TicketsWithIterationsPeriod')
async def get_tickets_with_iterations_period():
    return await get_repsonse_async(
        server_repository.get_tickets_with_iterations_period()
    )


@app.get('/CustomersGroups')
async def get_customers_groups(tracked: bool = False):
    return await get_repsonse_async(
        server_repository.get_tracked_customers_groups()
        if tracked else
        server_repository.get_customers_groups()
    )


@app.get('/TicketsTypes')
async def get_tickets_types():
    return await get_repsonse_async(
        server_repository.get_tickets_types()
    )


@app.get('/Frameworks')
async def get_frameworks():
    return await get_repsonse_async(
        server_repository.get_frameworks()
    )


@app.get('/OperatingSystems')
async def get_operating_systems():
    return await get_repsonse_async(
        server_repository.get_operating_systems()
    )


@app.get('/Builds')
async def get_builds():
    return await get_repsonse_async(
        server_repository.get_builds()
    )


@app.get('/SeverityValues')
async def get_severity_values():
    return await get_repsonse_async(
        server_repository.get_severity_values()
    )


@app.get('/TicketStatuses')
async def get_ticket_statuses():
    return await get_repsonse_async(
        server_repository.get_ticket_statuses()
    )


@app.get('/Ides')
async def get_ides():
    return await get_repsonse_async(
        server_repository.get_ides()
    )


@app.get('/TicketsTags')
async def get_tickets_tags():
    return await get_repsonse_async(
        server_repository.get_tickets_tags()
    )


@app.get('/CATRepliesTypes')
async def get_cat_get_replies_types():
    return await get_repsonse_async(
        server_repository.get_cat_replies_types()
    )


@app.post('/CATComponents')
async def get_cat_components(params: TentsParams):
    return await get_repsonse_async(
        server_repository.get_cat_components(
            tent_ids=params.tents,
        )
    )


@app.post('/CATFeatures')
async def get_cat_features(params: FeatureParams):
    return await get_repsonse_async(
        server_repository.get_cat_features(
            tent_ids=params.tents,
            component_ids=params.components,
        )
    )


@app.post('/Platforms')
async def get_platforms(params: TentsParams):
    return await get_repsonse_async(
        server_repository.get_platforms(
            tent_ids=params.tents,
        )
    )


@app.post('/Products')
async def get_products(params: TentsParams):
    return await get_repsonse_async(
        server_repository.get_products(
            tent_ids=params.tents,
        )
    )


@app.get('/GroupByPeriods')
async def get_group_by_periods():
    return await get_repsonse_async(
        server_repository.get_group_by_periods()
    )


# yapf: enable
@app.get('/PeriodsArray')
async def get_periods_array(
    start: str,
    end: str,
    format: str,
):
    return await get_repsonse_async(
        server_repository.get_periods_array(
            start=start,
            end=end,
            format=format,
        )
    )


@app.get('/LicenseStatuses')
async def get_license_statuses():
    return await get_repsonse_async(server_repository.get_license_statuses())


@app.post('/ConversionStatuses')
async def get_conversion_statuses(params: ConversionStatusParams):
    return await get_repsonse_async(
        server_repository.get_conversion_statuses(
            license_status_ids=params.license_statuses
        )
    )


@app.get('/Positions')
async def get_emp_positions():
    return await get_repsonse_async(server_repository.get_emp_positions())


@app.get('/EmpTribes')
async def get_emp_tribes():
    return await get_repsonse_async(server_repository.get_emp_tribes())


@app.get('/EmpTents')
async def get_emp_tents():
    return await get_repsonse_async(server_repository.get_emp_tents())


@app.post('/Employees')
async def get_employees(params: EmployeeParams):
    return await get_repsonse_async(
        server_repository.get_employees(
            position_ids=params.positions,
            tribe_ids=params.tribes,
            tent_ids=params.tents,
        )
    )


@app.post('/Customers')
async def get_customers(
    params: CustomersParams,
    search: str = '',
    skip: int = 0,
    take: int = 0,
):
    return await get_repsonse_async(
        server_repository.get_customers(
            filter_values=params.customers,
            search=search,
            skip=skip,
            take=take,
        )
    )


@app.post('/ValidateCustomers')
async def validate_customers(params: CustomersParams):
    return await get_repsonse_async(
        server_repository.validate_customers(values=params.customers)
    )


@app.post('/TicketsWithIterationsAggregates')
async def get_tickets_with_iterations_aggregates(
    group_by_period: str,
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
):
    return await get_repsonse_async(
        server_repository.get_tickets_with_iterations_aggregates(
            group_by_period=group_by_period,
            range_start=range_start,
            range_end=range_end,
            use_baseline_aligned_mode=baseline_aligned_mode_enabled,
            **body.get_field_values(),
        )
    )


@app.post('/TicketsWithIterationsRaw')
async def get_tickets_with_iterations_raw(
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
):
    return await get_repsonse_async(
        server_repository.get_tickets_with_iterations_raw(
            range_start=range_start,
            range_end=range_end,
            use_baseline_aligned_mode=baseline_aligned_mode_enabled,
            **body.get_field_values(),
        )
    )


@app.post('/DisplayFilter')
async def get_display_filter(body: TicketsWithIterationsParams):
    return await get_repsonse_async(server_repository.get_display_filter(body))


@app.get('/Help')
async def get_help():
    return await get_repsonse_async(help_index.get_descriptions())


@app.post('/PushState')
def push_state(params: ViewState):
    state_id = view_state_cache.push_state(params.state)
    return get_response(json_data=state_id)


@app.get('/PullState')
def pull_state(state_id: str):
    state = view_state_cache.pull_state(state_id)
    return get_response(json_data=state)
