from sql_queries.index import (
    CustomersActivityIndex,
)


def test_correct_root():
    fs = '/'
    assert CustomersActivityIndex.get_root_path().startswith(fs) == False
