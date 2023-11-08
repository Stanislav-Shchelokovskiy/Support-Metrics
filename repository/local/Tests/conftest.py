import pytest
import toolbox.sql.generators.Tests.filter_cases as filter_cases


@pytest.fixture(scope='module')
def single_in_filter_cases():
    return filter_cases.single_in_filter_cases


@pytest.fixture(scope='module')
def double_in_filter_cases():
    return filter_cases.double_in_filter_cases


@pytest.fixture
def single_like_filter_cases():
    return filter_cases.single_like_filter_cases()


@pytest.fixture
def between_filter_cases():
    return filter_cases.between_filter_cases


@pytest.fixture
def equals_filter_cases():
    return filter_cases.equals_filter_cases


@pytest.fixture
def less_equals_filter_cases():
    return filter_cases.less_equals_filter_cases
