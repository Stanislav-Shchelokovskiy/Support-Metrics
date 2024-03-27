import os
import help.index as help_index
import toolbox.cache.async_cache.view_state_cache as view_state_cache
from fastapi import FastAPI, status, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from prometheus_client import make_asgi_app
from repository import LocalRepository
from toolbox.utils.fastapi.decorators import with_authorization, AuthResponse
from toolbox.utils.converters import JSON_to_object
from toolbox.sql.aggs.metrics_usage import track_metric_usage
from server_models import (
    TicketsWithIterationsParams,
    TentsParams,
    FeatureParams,
    ViewState,
    ConversionStatusParams,
    EmployeeParams,
    CustomersParams,
)


class CustomJSONResponse(Response):
    media_type = 'application/json'


app = FastAPI(default_response_class=CustomJSONResponse)

origins = JSON_to_object.convert(os.environ['CORS_ORIGINS'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


async def check_status(response: AuthResponse):
    return response.status == status.HTTP_200_OK


# yapf: disable
@app.get('/TicketsWithIterationsPeriod')
async def get_tickets_with_iterations_period():
    return await LocalRepository.tickets_with_iterations_period.get_data()


@app.get('/CustomersGroups')
async def get_customers_groups(tracked: bool = False):
    return await (
        LocalRepository.tracked_customers_groups.get_data()
        if tracked else
        LocalRepository.customers_groups.get_data()
    )


@app.get('/TicketsTypes')
async def get_tickets_types():
    return await LocalRepository.tickets_types.get_data()


@app.get('/Frameworks')
async def get_frameworks():
    return await LocalRepository.frameworks.get_data()


@app.get('/OperatingSystems')
async def get_operating_systems():
    return await LocalRepository.operating_systems.get_data()


@app.get('/Builds')
async def get_builds():
    return await LocalRepository.builds.get_data()


@app.get('/SeverityValues')
async def get_severity_values():
    return await LocalRepository.severity.get_data()


@app.get('/TicketStatuses')
async def get_ticket_statuses():
    return await LocalRepository.ticket_statuses.get_data()


@app.get('/Ides')
async def get_ides():
    return await LocalRepository.ides.get_data()


@app.get('/TicketsTags')
async def get_tickets_tags():
    return await LocalRepository.tickets_tags.get_data()


@app.get('/CATRepliesTypes')
async def get_cat_get_replies_types():
    return await LocalRepository.replies_types.get_data()


@app.post('/CATComponents')
async def get_cat_components(params: TentsParams):
    return await LocalRepository.components.get_data(
            tent_ids=params.tents
        )

@app.post('/CATFeatures')
async def get_cat_features(params: FeatureParams):
    return await LocalRepository.features.get_data(
            tent_ids=params.tents,
            component_ids=params.components,
        )


@app.post('/Platforms')
async def get_platforms(params: TentsParams):
    return await LocalRepository.platforms.get_data(
            tent_ids=params.tents
        )


@app.post('/Products')
async def get_products(params: TentsParams):
    return await LocalRepository.products.get_data(
            tent_ids=params.tents
        )


@app.get('/GroupByPeriods')
async def get_group_by_periods():
    return await LocalRepository.get_group_by_periods()


# yapf: enable
@app.get('/PeriodsArray')
async def get_periods_array(
    start: str,
    end: str,
    format: str,
):
    return await LocalRepository.get_periods_array(
        start=start,
        end=end,
        format=format,
    )


@app.get('/LicenseStatuses')
async def get_license_statuses():
    return await LocalRepository.license_statuses.get_data()


@app.post('/ConversionStatuses')
async def get_conversion_statuses(params: ConversionStatusParams):
    return await LocalRepository.conversion_statuses.get_data(
        license_status_ids=params.license_statuses
    )


@app.get('/Positions')
async def get_emp_positions():
    return await LocalRepository.emp_positions.get_data()


@app.get('/EmpTribes')
async def get_emp_tribes():
    return await LocalRepository.emp_tribes.get_data()


@app.get('/EmpTents')
async def get_emp_tents():
    return await LocalRepository.emp_tents.get_data()


@app.get('/Roles')
async def get_roles():
    return await LocalRepository.roles.get_data()


@app.get('/Tents')
async def get_tents():
    return await LocalRepository.tents.get_data()


@app.get('/Tribes')
async def get_tribes():
    return await LocalRepository.tribes.get_data()


@app.post('/Employees')
async def get_employees(body: EmployeeParams):
    return await LocalRepository.employees.get_data(
        **body.get_field_values(),
    )


@app.post('/Customers')
async def get_customers(
    params: CustomersParams,
    search: str = '',
    skip: int = 0,
    take: int = 0,
):
    return await LocalRepository.customers.get_data(
        filter_values=params.customers,
        search=search,
        skip=skip,
        take=take,
    )


@app.post('/ValidateCustomers')
async def validate_customers(params: CustomersParams):
    return await LocalRepository.customers_validation.validate_data(
        values=params.customers
    )


@app.post('/TicketsWithIterationsAggregates')
@with_authorization(check_status)
@track_metric_usage(LocalRepository.metrics, 'support_metrics')
async def get_tickets_with_iterations_aggregates(
    group_by_period: str,
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
    response: Response,
    access_token: str | None = Header(None, alias='Authorization'),
    metric: str = None,
):
    return await LocalRepository.tickets_with_iterations_aggregates.get_data(
        group_by_period=group_by_period,
        range_start=range_start,
        range_end=range_end,
        use_baseline_aligned_mode=baseline_aligned_mode_enabled,
        metric=metric,
        **body.get_field_values(),
    )


@app.post('/TicketsWithIterationsRaw')
@with_authorization(check_status)
async def get_tickets_with_iterations_raw(
    range_start: str,
    range_end: str,
    baseline_aligned_mode_enabled: bool,
    body: TicketsWithIterationsParams,
    response: Response,
    access_token: str | None = Header(None, alias='Authorization'),
):
    return await LocalRepository.tickets_with_iterations_raw.get_data(
        range_start=range_start,
        range_end=range_end,
        use_baseline_aligned_mode=baseline_aligned_mode_enabled,
        **body.get_field_values(),
    )


@app.post('/DisplayFilter')
async def get_display_filter(body: TicketsWithIterationsParams):
    return await LocalRepository.get_display_filter(body)


@app.get('/Help')
async def get_help():
    return await help_index.get_descriptions()


@app.get('/Help/MetricDescription')
async def get_metric_description(metric: str):
    return await help_index.get_description(metric)


@app.get('/Metrics')
async def get_metrics():
    return await LocalRepository.get_metrics()


@app.post('/PushState')
@with_authorization(check_status)
async def push_state(
    body: ViewState,
    response: Response,
    access_token: str | None = Header(None, alias='Authorization'),
):
    return await view_state_cache.push_state(body.state)


@app.get('/PullState', status_code=status.HTTP_200_OK)
@with_authorization(check_status)
async def pull_state(
    state_id: str,
    response: Response,
    access_token: str | None = Header(None, alias='Authorization'),
):
    state = await view_state_cache.pull_state(state_id)
    if not state:
        response.status_code = status.HTTP_404_NOT_FOUND
    return state


metrics_app = make_asgi_app()
app.mount('/metrics', metrics_app)
