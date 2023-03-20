from sql_queries.index import (
    CustomersActivitySqlPathIndex,
)


def test_correct_root():
    fs = '/'
    assert CustomersActivitySqlPathIndex.get_root_path().startswith(fs) is False
