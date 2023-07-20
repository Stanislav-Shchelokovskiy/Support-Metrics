import pytest
from Tests.utils import (
    response_is_valid,
    network_get,
    network_post,
)


@pytest.mark.e2e
def test_get_tickets_with_iterations_period(test_client):
    response = network_get(
        client=test_client,
        url='TicketsWithIterationsPeriod',
    )
    assert response == '[{"period_start":"2022-07-01","period_end":"2022-12-31"}]'


@pytest.mark.e2e
def test_get_customers_activity_display_filter(test_client):
    response = network_post(
        client=test_client,
        url='DisplayFilter',
        body='display_filter',
    )
    assert response_is_valid(
        file='display_filter',
        check_file='display_filter',
        response=response,
    )


@pytest.mark.e2e
def test_get_customers_activity_validate_customers(test_client):
    response = network_post(
        client=test_client,
        url='ValidateCustomers',
        body='validate_customers',
    )
    assert response_is_valid(
        file='validate_customers',
        check_file='validate_customers',
        response=response,
    )


@pytest.mark.e2e
@pytest.mark.parametrize(
    'file_name, bam', [
        ('conversion_rate', False),
        ('emp_replies_wpf', False),
        ('emp_replies_asp', False),
        ('emp_replies_devextreme', False),
        ('reply_type_is_missing', False),
        ('asp_blazor_income', False),
        ('xaf_support_replies', False),
        ('xaf_pm_replies', False),
        ('bam_mau_under_review_devextreme', True),
        ('bam_mau_ray', True),
        ('median', False),
        ('reports_export_to_pdf', False),
        ('customer', False),
        ('devextreme_contribution', False),
    ]
)
def test_get_tickets_with_iterations_aggregates(file_name, bam, test_client):
    response = network_post(
        client=test_client,
        url=r'TicketsWithIterationsAggregates?group_by_period=%Y-%m&range_start={start_date}&range_end={end_date}&baseline_aligned_mode_enabled='
        + str(bam),
        body=f'tickets_with_iterations/{file_name}',
    )
    assert response_is_valid(
        file=file_name,
        check_file=f'tickets_with_iterations_aggregates/{file_name}',
        response=response,
    )


@pytest.mark.e2e
@pytest.mark.parametrize(
    'file_name, bam', [
        ('conversion_rate', False),
        ('emp_replies_wpf', False),
        ('emp_replies_asp', False),
        ('emp_replies_devextreme', False),
        ('reply_type_is_missing', False),
        ('asp_blazor_income', False),
        ('xaf_support_replies', False),
        ('xaf_pm_replies', False),
        ('bam_mau_under_review_devextreme', True),
        ('bam_mau_ray', True),
        ('median', False),
        ('reports_export_to_pdf', False),
        ('customer', False),
        ('devextreme_contribution', False),
    ]
)
def test_get_tickets_with_iterations_raw(file_name, bam, test_client):
    response = network_post(
        client=test_client,
        url=r'TicketsWithIterationsRaw?range_start={start_date}&range_end={end_date}&baseline_aligned_mode_enabled='
        + str(bam),
        body=f'tickets_with_iterations/{file_name}',
    )
    assert response_is_valid(
        file=file_name,
        check_file=f'tickets_with_iterations_raw/{file_name}',
        response=response,
    )


@pytest.mark.e2e
@pytest.mark.parametrize('file_name', [
    'y',
    'ym',
    'ymd',
    'yw',
])
def test_get_periods_array(file_name, test_client):
    response = network_get(
        client=test_client,
        url='PeriodsArray',
        params=f'periods_array/{file_name}',
    )
    assert response_is_valid(
        file=file_name,
        check_file=f'periods_array/{file_name}',
        response=response,
    )