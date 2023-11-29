from pydantic import Field, validator
from repository.local.core.customers_rank import Percentile as percentile_validator
from toolbox.server_models import (
    ServerModel,
    FilterParameterNode,
    FilterParametersNode,
    ViewState,
)
from toolbox.sql.generators import (between, notbetwen, ge, lt, right_half_open, not_right_half_open)


class TentsParams(ServerModel):
    tents: FilterParametersNode[str]


class FeatureParams(TentsParams):
    components: FilterParametersNode[str]


class EmployeeParams(ServerModel):
    position_ids: FilterParametersNode[str] = Field(alias='positions')
    tribe_ids: FilterParametersNode[str]= Field(alias='tribes')
    tent_ids: FilterParametersNode[str]= Field(alias='tents')
    role_ids: FilterParametersNode[str]= Field(alias='roles')


class ConversionStatusParams(ServerModel):
    license_statuses: FilterParametersNode[int]


class CustomersParams(ServerModel):
    customers: list[str]


class Percentile(ServerModel):
    metric: str
    value: FilterParameterNode[int]

    @validator('metric')
    def to_valid_literal(cls, v: str):
        return percentile_validator.to_valid_literal(v)


# yapf: disable
class TicketsWithIterationsParams(ServerModel):
    percentile: Percentile = Field(alias='Percentile')
    is_private: FilterParameterNode[int] | None = Field(alias='Ticket visibility')
    is_employee: FilterParameterNode[int] | None = Field(alias='Ticket owner')
    tribe_ids: FilterParametersNode[str] | None = Field(alias='Tribes')
    tent_ids: FilterParametersNode[str] | None = Field(alias='Tents')
    platforms_ids: FilterParametersNode[str] | None = Field(alias='Platforms')
    products_ids: FilterParametersNode[str] | None = Field(alias='Products')
    tickets_tags: FilterParametersNode[str] | None = Field(alias='Ticket tags')
    tickets_types: FilterParametersNode[int] | None = Field(alias='Ticket types')
    duplicated_to_tickets_types: FilterParametersNode[int] | None = Field(alias='Duplicated to ticket types')
    builds: FilterParametersNode[str] | None = Field(alias='Versions')
    fixed_in_builds: FilterParametersNode[str] | None = Field(alias='Fixed In')
    severity: FilterParametersNode[str] | None = Field(alias='Severity')
    ticket_status: FilterParametersNode[str] | None = Field(alias='Ticket statuses')
    operating_system_id: FilterParametersNode[str] | None = Field(alias='Operating systems')
    frameworks: FilterParametersNode[str] | None = Field(alias='Frameworks/Specifics')
    ide_id: FilterParametersNode[str] | None = Field(alias='IDE')
    customers_groups: FilterParametersNode[str] | None = Field(alias='User groups')
    license_statuses: FilterParametersNode[int] | None = Field(alias='User types')
    conversion_statuses: FilterParametersNode[int] | None = Field(alias='User conversion types')
    positions_ids: FilterParametersNode[str] | None = Field(alias='Employees positions')
    emp_tribe_ids: FilterParametersNode[str] | None = Field(alias='Employees tribes')
    emp_tent_ids: FilterParametersNode[str] | None = Field(alias='Employees tents')
    roles: FilterParametersNode[str] | None = Field(alias='Roles')
    emp_ids: FilterParametersNode[str] | None = Field(alias='Employees')
    assigned_to_ids: FilterParametersNode[str] | None = Field(alias='Assigned to')
    closed_by_ids: FilterParametersNode[str] | None = Field(alias='Closed by')
    closed_between: FilterParametersNode[str] | None = Field(alias='Closed', positive_filter_op=between, negative_filter_op=notbetwen)
    closed_for_n_days: FilterParameterNode[int] | None = Field(alias='Closed for', positive_filter_op=ge, negative_filter_op=lt)
    resolution_in_hours: FilterParametersNode[int] | None = Field(alias='Resolution time', positive_filter_op=right_half_open, negative_filter_op=not_right_half_open)
    fixed_by_ids: FilterParametersNode[str] | None = Field(alias='Fixed by')
    fixed_between: FilterParametersNode[str] | None = Field(alias='Fixed', positive_filter_op=between, negative_filter_op=notbetwen)
    reply_ids: FilterParametersNode[str] | None = Field(alias='CAT replies types')
    components_ids: FilterParametersNode[str] | None = Field(alias='CAT components')
    feature_ids: FilterParametersNode[str] | None = Field(alias='CAT features')
    customers_crmids: FilterParametersNode[str] | None = Field(alias='Customers')
# yapf: enable
