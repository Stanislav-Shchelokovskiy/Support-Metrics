import pytest
from Tests.utils import (
    response_is_valid,
    network_get,
    network_post,
)


@pytest.mark.e2e
def test_get_tickets_with_iterations_period():
    assert network_get(
        url='get_tickets_with_iterations_period'
    ) == '[{"period_start":"2022-07-01","period_end":"2022-12-31"}]'


@pytest.mark.e2e
def test_get_customers_activity_display_filter():
    response = network_post(
        url='get_customers_activity_display_filter',
        body='display_filter',
    )
    assert response_is_valid(
        file='display_filter',
        check_file='display_filter',
        response=response,
    )

@pytest.mark.e2e
def test_get_customers_activity_validate_customers():
    response = network_post(
        url='validate_customers',
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
def test_get_tickets_with_iterations_aggregates(file_name, bam):
    response = network_post(
        url=r'get_tickets_with_iterations_aggregates?group_by_period=%Y-%m&range_start={start_date}&range_end={end_date}&baseline_aligned_mode_enabled='
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
def test_get_tickets_with_iterations_raw(file_name, bam):
    response = network_post(
        url=r'get_tickets_with_iterations_raw?range_start={start_date}&range_end={end_date}&baseline_aligned_mode_enabled='
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
def test_get_periods_array(file_name):
    response = network_get(
        url='get_periods_array',
        params=f'periods_array/{file_name}',
    )
    assert response_is_valid(
        file=file_name,
        check_file=f'periods_array/{file_name}',
        response=response,
    )
