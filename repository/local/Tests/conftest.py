import pytest
import toolbox.sql.generators.Tests.filter_cases as filter_cases


@pytest.fixture
def single_in_filter_cases():
    return filter_cases.single_in_filter_cases


@pytest.fixture
def double_in_filter_cases():
    return filter_cases.double_in_filter_cases


@pytest.fixture
def single_like_filter_cases():
    return filter_cases.single_like_filter_cases


@pytest.fixture
def between_filter_cases():
    return filter_cases.between_filter_cases


@pytest.fixture
def equals_filter_cases():
    return filter_cases.equals_filter_cases


@pytest.fixture
def less_equals_filter_cases():
    return filter_cases.less_equals_filter_cases


@pytest.fixture
def right_halfopen_interval_filter_cases():
    return filter_cases.right_half_open_interval_filter_cases
