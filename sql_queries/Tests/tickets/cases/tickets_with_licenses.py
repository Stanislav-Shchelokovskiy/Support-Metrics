from sql_queries.meta.aggs import TicketsWithIterations
from sql_queries.Tests.tickets.cases.licenses import _lcs
import sql_queries.index.path.remote as _path_index


class __twl:
    specifics = 'specifics'
    ticket_platforms = 'ticket_platforms'
    ticket_products = 'ticket_products'
    free = 'free'
    licensed_platforms = 'licensed_platforms'
    licensed_products = 'licensed_products'
    suitability = 'suitability'


want = {
    TicketsWithIterations.user_crmid.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000005'
        ],
    TicketsWithIterations.user_register_date.name:
        [
            '2022-01-01', '2022-01-01', '2022-01-01', '1990-01-01',
            '1990-01-01', '1990-01-01', '1990-01-01', '2022-03-01',
            '2022-03-01', '2022-03-01', '2022-04-01', '2022-04-01',
            '2022-04-01', '2022-04-01', '2022-04-01'
        ],
    TicketsWithIterations.user_id.name:
        [
            'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2',
            'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user4',
            'user5'
        ],
    TicketsWithIterations.is_employee.name:
        [
            False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False
        ],
    TicketsWithIterations.ticket_id.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000006',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000005',
            '00000000-0000-0000-0000-000000000009',
            '00000000-0000-0000-0000-000000000011',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000008',
            '00000000-0000-0000-0000-000000000010',
            '00000000-0000-0000-0000-000000000012',
            '00000000-0000-0000-0000-000000000013',
            '00000000-0000-0000-0000-000000000014',
            '00000000-0000-0000-0000-000000000015',
            '00000000-0000-0000-0000-000000000003'
        ],
    TicketsWithIterations.ticket_scid.name:
        [
            'trial (11)', 'licensed (0)', 'expired (2)', 'licensed (0)',
            'revoked (3)', 'no_license_revoked (6)',
            'no_license_expired_revoked (8)', 'no license (5)', 'licensed (0)',
            'no_license_expired (7)', 'trial (11)', 'no_license_free (9)',
            'no_license_expired_free (10)', 'free (1)',
            'assigned_to_someone (4)'
        ],
    TicketsWithIterations.ticket_type.name:
        [1, 1, 1, 1, 1, 1, 1, 2, 6, 2, 1, 1, 1, 1, 1],
    TicketsWithIterations.creation_date.name:
        [
            '2023-02-01', '2023-07-01', '2024-06-02', '2024-01-01',
            '2024-04-02', '2024-04-02', '2024-07-02', '2023-02-02',
            '2023-02-03', '2024-02-02', '2023-01-02', '2023-03-02',
            '2024-03-02', '2023-03-02', '2023-08-01'
        ],
    TicketsWithIterations.is_private.name:
        [
            True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True
        ],
    __twl.specifics:
        [
            None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000001', None, None, None, None,
            None, None, None, None
        ],
    TicketsWithIterations.builds.name:
        [
            None, None, None, None, None, None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000001', None, None, None
        ],
    TicketsWithIterations.fixed_in_builds.name:
        [
            None, None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000007', None, None, None, None,
            None, None, None
        ],
    __twl.ticket_platforms:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000004', None,
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None, None,
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None, None, None, None,
            None, '00000000-0000-0000-0000-000000000002'
        ],
    __twl.ticket_products:
        [
            None, None, '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000011',
            '00000000-0000-0000-0000-000000000001', None,
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000011',
            '00000000-0000-0000-0000-000000000006'
        ],
    _lcs.owner_crmid:
        [
            None, '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None, None, None,
            '00000000-0000-0000-0000-000000000003', None, None, None, None,
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000005'
        ],
    _lcs.end_user_crmid:
        [
            None, '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002', None, None, None,
            '00000000-0000-0000-0000-000000000003', None, None, None, None,
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000005'
        ],
    _lcs.lic_origin:
        [
            None,
            0,
            0,
            1,
            1,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            None,
            0,
            1,
        ],
    _lcs.revoked_since:
        [
            None, None, None, '2024-02-01', '2024-02-01', None, None, None,
            None, None, None, None, None, None, '2023-07-01'
        ],
    TicketsWithIterations.subscription_start.name:
        [
            None, '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', None,
            None, None, '2023-01-01', None, None, None, None, '2023-02-01',
            '2023-01-01'
        ],
    TicketsWithIterations.expiration_date.name:
        [
            None, '2024-05-31', '2024-05-31', '2024-05-31', '2024-05-31', None,
            None, None, '2024-01-01', None, None, None, None, '2024-02-01',
            '2024-01-01'
        ],
    __twl.free:
        [None, 5, 5, 5, 5, None, None, None, 5, None, None, None, None, 6, 5],
    TicketsWithIterations.license_name.name:
        [
            None, 'free bundle', 'dxp', 'dxp', 'dxp', None, None, None,
            'devextreme', None, None, None, None, 'devextreme', 'dxp'
        ],
    TicketsWithIterations.parent_license_name.name:
        [
            None, 'dxp', None, None, None, None, None, None, None, None, None,
            None, None, None, None
        ],
    __twl.licensed_platforms:
        [
            None, '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002', None, None, None,
            '00000000-0000-0000-0000-000000000002', None, None, None, None,
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002'
        ],
    __twl.licensed_products:
        [
            None,
            '00000000-0000-0000-0000-000000000012;00000000-0000-0000-0000-000000000013;00000000-0000-0000-0000-000000000014;00000000-0000-0000-0000-000000000015',
            '00000000-0000-0000-0000-000000000005;00000000-0000-0000-0000-000000000006;00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000005;00000000-0000-0000-0000-000000000006;00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000005;00000000-0000-0000-0000-000000000006;00000000-0000-0000-0000-000000000007',
            None, None, None,
            '00000000-0000-0000-0000-000000000008;00000000-0000-0000-0000-000000000009;00000000-0000-0000-0000-000000000010;00000000-0000-0000-0000-000000000011',
            None, None, None, None,
            '00000000-0000-0000-0000-000000000008;00000000-0000-0000-0000-000000000009;00000000-0000-0000-0000-000000000010;00000000-0000-0000-0000-000000000011',
            '00000000-0000-0000-0000-000000000008;00000000-0000-0000-0000-000000000009;00000000-0000-0000-0000-000000000010;00000000-0000-0000-0000-000000000011'
        ],
    __twl.suitability:
        [None, 1, 2, 1, 3, None, None, None, 0, None, None, None, None, 0, 3],
    TicketsWithIterations.license_status.name:
        [11, 0, 2, 0, 3, 6, 8, 5, 0, 7, 11, 9, 10, 1, 4],
}

queries = (
    _path_index.sale_item_platforms,
    _path_index.sale_tem_products,
    _path_index.sale_items_flat,
    _path_index.licenses,
    _path_index.tickets_with_licenses,
)

params = {
    'start_date': '2022-01-01',
    'end_date': '2025-01-01',
}

dtfields = (
    TicketsWithIterations.user_register_date.name,
    TicketsWithIterations.creation_date.name,
    _lcs.revoked_since,
    TicketsWithIterations.subscription_start.name,
    TicketsWithIterations.expiration_date.name,
)

tbl = '#TicketsWithLicenses'
