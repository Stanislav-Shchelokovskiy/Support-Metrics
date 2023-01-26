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
    ) == '{"period_start":"2022-07-01","period_end":"2022-12-31"}'


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
@pytest.mark.parametrize(
    'file_name', [
        'conversion_rate',
        'emp_replies_wpf',
        'emp_replies_asp',
        'emp_replies_devextreme',
        'reply_type_is_missing',
        'asp_blazor_income',
        'xaf_support_replies',
        'xaf_pm_replies',
        'mau_under_review_devextreme_baseline_alignment',
        'median',
        'reports_export_to_pdf',
        'customer',
    ]
)
def test_get_tickets_with_iterations_aggregates(file_name):
    response = network_post(
        url=r'get_tickets_with_iterations_aggregates?group_by_period=%Y-%m&range_start={start_date}&range_end={end_date}&baseline_aligned_mode_enabled=false',
        body=f'tickets_with_iterations/{file_name}',
    )
    assert response_is_valid(
        file=file_name,
        check_file=f'tickets_with_iterations_aggregates/{file_name}',
        response=response,
    )


@pytest.mark.e2e
@pytest.mark.parametrize(
    'file_name', [
        'conversion_rate',
        'emp_replies_wpf',
        'emp_replies_asp',
        'emp_replies_devextreme',
        'reply_type_is_missing',
        'asp_blazor_income',
        'xaf_support_replies',
        'xaf_pm_replies',
        'mau_under_review_devextreme_baseline_alignment',
        'median',
        'reports_export_to_pdf',
        'customer',
    ]
)
def test_get_tickets_with_iterations_raw(file_name):
    response = network_post(
        url=r'get_tickets_with_iterations_raw?range_start={start_date}&range_end={end_date}&baseline_aligned_mode_enabled=false',
        body=f'tickets_with_iterations/{file_name}',
    )
    assert response_is_valid(
        file=file_name,
        check_file=f'tickets_with_iterations_raw/{file_name}',
        response=response,
    )
