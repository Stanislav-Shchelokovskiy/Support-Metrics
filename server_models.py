from pydantic import Field
from toolbox.server_models import (
    ServerModel,
    FilterParameterNode,
    FilterParametersNode,
    ViewState,
)


class TentsParams(ServerModel):
    tents: FilterParametersNode


class FeatureParams(TentsParams):
    components: FilterParametersNode


class EmployeeParams(ServerModel):
    positions: FilterParametersNode
    tribes: FilterParametersNode
    tents: FilterParametersNode


class ConversionStatusParams(ServerModel):
    license_statuses: FilterParametersNode


class CustomersParams(ServerModel):
    customers: list[str]


class Percentile(ServerModel):
    metric: str
    value: FilterParameterNode


# yapf: disable
class TicketsWithIterationsParams(ServerModel):
    percentile: Percentile = Field(alias='Percentile')
    is_private: FilterParameterNode | None = Field(alias='Privacy')
    tribe_ids: FilterParametersNode | None = Field(alias='Tribes')
    tent_ids: FilterParametersNode | None = Field(alias='Tents')
    platforms_ids: FilterParametersNode | None = Field(alias='Platforms')
    products_ids: FilterParametersNode | None = Field(alias='Products')
    tickets_tags: FilterParametersNode | None = Field(alias='Ticket tags')
    tickets_types: FilterParametersNode | None = Field(alias='Ticket types')
    duplicated_to_tickets_types: FilterParametersNode | None = Field(alias='Duplicated to ticket types')
    builds: FilterParametersNode | None = Field(alias='Versions')
    fixed_in_builds: FilterParametersNode | None = Field(alias='Fixed In')
    severity: FilterParametersNode | None = Field(alias='Severity')
    ticket_status: FilterParametersNode | None = Field(alias='Ticket statuses')
    operating_system_id: FilterParametersNode | None = Field(alias='Operating systems')
    frameworks: FilterParametersNode | None = Field(alias='Frameworks/Specifics')
    ide_id: FilterParametersNode | None = Field(alias='IDE')
    customers_groups: FilterParametersNode | None = Field(alias='User groups')
    license_statuses: FilterParametersNode | None = Field(alias='User types')
    conversion_statuses: FilterParametersNode | None = Field(alias='User conversion types')
    positions_ids: FilterParametersNode | None = Field(alias='Employees positions')
    emp_tribe_ids: FilterParametersNode | None = Field(alias='Employees tribes')
    emp_tent_ids: FilterParametersNode | None = Field(alias='Employees tents')
    emp_ids: FilterParametersNode | None = Field(alias='Employees')
    assigned_to_ids: FilterParametersNode | None = Field(alias='Assigned to')
    closed_by_ids: FilterParametersNode | None = Field(alias='Closed by')
    closed_between: FilterParametersNode | None = Field(alias='Closed', positive_filter_op='between', negative_filter_op='notbetween')
    fixed_by_ids: FilterParametersNode | None = Field(alias='Fixed by')
    fixed_between: FilterParametersNode | None = Field(alias='Fixed', positive_filter_op='between', negative_filter_op='notbetween')
    reply_ids: FilterParametersNode | None = Field(alias='CAT replies types')
    components_ids: FilterParametersNode | None = Field(alias='CAT components')
    feature_ids: FilterParametersNode | None = Field(alias='CAT features')
    customers_crmids: FilterParametersNode | None = Field(alias='Customers')
# yapf: enable
