import pytest
from repository.customers_activity.local.Tests.mocks import MockFilterParametersNode


# yapf: disable
@pytest.fixture(scope='module')
def single_in_filter_cases():

    def cases(convert, prefix='WHERE'):
        convert = convert or (lambda val: f"'{val}'")
        return [
            (
                None,
                '',
            ),
            (
                MockFilterParametersNode(include=True, values=[]),
                '',
            ),
            (
                MockFilterParametersNode(include=False, values=[]),
                prefix + ' {field} IS NULL',
            ),
            (
                MockFilterParametersNode(include=True, values=[123]),
                prefix + ' {field} IN ' + f'({convert(123)})',
            ),
            (
                MockFilterParametersNode(include=False, values=[123]),
                prefix + ' ({field} IS NULL OR {field} NOT IN ' + f'({convert(123)}))',
            ),
            (
                MockFilterParametersNode(include=True, values=[1, 2]),
                prefix + ' {field} IN ' + f'({convert(1)},{convert(2)})',
            ),
            (
                MockFilterParametersNode(include=False, values=[1, 2]),
                prefix + ' ({field} IS NULL OR {field} NOT IN ' + f'({convert(1)},{convert(2)}))',
            ),
        ]

    return cases


@pytest.fixture(scope='module')
def double_in_filter_cases():

    def cases(convert, prefix='WHERE'):
        convert = convert or (lambda val: f"'{val}'")
        return [
            (
                None,
                None,
                '',
            ),
            (
                MockFilterParametersNode(include=True, values=[]),
                None,
                '',
            ),
            (
                MockFilterParametersNode(include=True, values=[]),
                MockFilterParametersNode(include=True, values=[]),
                '',
            ),
            (
                MockFilterParametersNode(include=False, values=[]),
                MockFilterParametersNode(include=True, values=[]),
                prefix + ' {field1} IS NULL',
            ),
            (
                MockFilterParametersNode(include=True, values=[]),
                MockFilterParametersNode(include=False, values=[]),
                prefix + ' {field2} IS NULL',
            ),
            (
                MockFilterParametersNode(include=False, values=[]),
                MockFilterParametersNode(include=False, values=[]),
                prefix + ' {field1} IS NULL AND {field2} IS NULL',
            ),
            (
                MockFilterParametersNode(include=True, values=[123]),
                MockFilterParametersNode(include=True, values=[]),
                prefix + ' {field1} IN ' + f'({convert(123)})',
            ),
            (
                MockFilterParametersNode(include=False, values=[123]),
                MockFilterParametersNode(include=True, values=[]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(123)}))',
            ),
            (
                MockFilterParametersNode(include=True, values=[123]),
                MockFilterParametersNode(include=False, values=[]),
                prefix + ' {field1} IN ' + f'({convert(123)})' + ' AND {field2} IS NULL',
            ),
            (
                MockFilterParametersNode(include=False, values=[123]),
                MockFilterParametersNode(include=False, values=[]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(123)}))' + ' AND {field2} IS NULL',
            ),
            (
                MockFilterParametersNode(include=True, values=[]),
                MockFilterParametersNode(include=True, values=[123]),
                prefix + ' {field2} IN ' + f'({convert(123)})',
            ),
            (
                MockFilterParametersNode(include=False, values=[]),
                MockFilterParametersNode(include=True, values=[123]),
                prefix + ' {field1} IS NULL AND {field2} IN ' + f'({convert(123)})',
            ),
            (
                MockFilterParametersNode(include=True, values=[]),
                MockFilterParametersNode(include=False, values=[123]),
                prefix + ' ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(123)}))',
            ),
            (
                MockFilterParametersNode(include=False, values=[]),
                MockFilterParametersNode(include=False, values=[123]),
                prefix + ' {field1} IS NULL AND ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(123)}))',
            ),
            (
                MockFilterParametersNode(include=True, values=[1]),
                MockFilterParametersNode(include=True, values=[2]),
                prefix + ' {field1} IN ' + f'({convert(1)})' + ' AND {field2} IN ' + f'({convert(2)})',
            ),
            (
                MockFilterParametersNode(include=False, values=[1]),
                MockFilterParametersNode(include=True, values=[2]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(1)}))' + ' AND {field2} IN ' + f'({convert(2)})',
            ),
            (
                MockFilterParametersNode(include=True, values=[1]),
                MockFilterParametersNode(include=False, values=[2]),
                prefix + ' {field1} IN ' + f'({convert(1)})' + ' AND ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(2)}))',
            ),
            (
                MockFilterParametersNode(include=False, values=[1]),
                MockFilterParametersNode(include=False, values=[2]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(1)}))' + ' AND ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(2)}))',
            ),
            (
                MockFilterParametersNode(include=True, values=[1, 2]),
                MockFilterParametersNode(include=True, values=[3, 4]),
                prefix + ' {field1} IN ' + f'({convert(1)},{convert(2)})' + ' AND {field2} IN ' + f'({convert(3)},{convert(4)})',
            ),
            (
                MockFilterParametersNode(include=False, values=[1, 2]),
                MockFilterParametersNode(include=True, values=[3, 4]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(1)},{convert(2)}))' + ' AND {field2} IN ' + f'({convert(3)},{convert(4)})',
            ),
            (
                MockFilterParametersNode(include=True, values=[1, 2]),
                MockFilterParametersNode(include=False, values=[3, 4]),
                prefix + ' {field1} IN ' + f'({convert(1)},{convert(2)})' + ' AND ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(3)},{convert(4)}))'
            ),
            (
                MockFilterParametersNode(include=False, values=[1, 2]),
                MockFilterParametersNode(include=False, values=[3, 4]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(1)},{convert(2)}))' + ' AND ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(3)},{convert(4)}))',
            ),
            (
                MockFilterParametersNode(include=True, values=[1, 2]),
                MockFilterParametersNode(include=True, values=[3]),
                prefix + ' {field1} IN ' + f'({convert(1)},{convert(2)})' + ' AND {field2} IN ' + f'({convert(3)})',
            ),
            (
                MockFilterParametersNode(include=False, values=[1, 2]),
                MockFilterParametersNode(include=True, values=[3]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(1)},{convert(2)}))' + ' AND {field2} IN ' + f'({convert(3)})',
            ),
            (
                MockFilterParametersNode(include=True, values=[1, 2]),
                MockFilterParametersNode(include=False, values=[3]),
                prefix + ' {field1} IN ' + f'({convert(1)},{convert(2)})' + ' AND ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(3)}))',
            ),
            (
                MockFilterParametersNode(include=False, values=[1, 2]),
                MockFilterParametersNode(include=False, values=[3]),
                prefix + ' ({field1} IS NULL OR {field1} NOT IN ' + f'({convert(1)},{convert(2)}))' + ' AND ({field2} IS NULL OR {field2} NOT IN ' + f'({convert(3)}))',
            ),
        ]

    return cases


@pytest.fixture
def single_like_filter_cases():
    return [
        (
            None,
            '',
        ),
        (
            MockFilterParametersNode(include=True, values=[]),
            '',
        ),
        (
            MockFilterParametersNode(include=False, values=[]),
            'AND {field} IS NULL',
        ),
        (
            MockFilterParametersNode(include=True, values=['p1', 'p2']),
            "AND ({field} LIKE '%p1%' OR {field} LIKE '%p2%')"
        ),
        (
            MockFilterParametersNode(include=True, values=['p1']),
            "AND ({field} LIKE '%p1%')"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1', 'p2']),
            "AND ({field} IS NULL OR NOT ({field} LIKE '%p1%' OR {field} LIKE '%p2%'))"
        ),
        (
            MockFilterParametersNode(include=False, values=['p1']),
            "AND ({field} IS NULL OR NOT ({field} LIKE '%p1%'))"
        ),
    ]
