from sql_queries.Tests.tickets.cases.sale_item.common import (
    _saleitem,
    dtfields,
    params,
    _path_index,
)


want = {
    _saleitem.sale_item_id:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000004',
        ],
    _saleitem.platform_id:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000004',
        ],
}

tbl = '#SaleItemPlatforms'
queries = [_path_index.sale_item_platforms]
