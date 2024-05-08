from sql_queries.meta.aggs import TicketsWithIterations


want = {
    TicketsWithIterations.user_crmid.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000005',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000004'
        ],
    TicketsWithIterations.user_id.name:
        [
            'user1', 'user1', 'user5', 'user2', 'user2', 'user1', 'user3',
            'user3', 'user2', 'user3', 'user2', 'user4', 'user4', 'user4',
            'user4'
        ],
    TicketsWithIterations.is_employee.name: [False] * 15,
    TicketsWithIterations.user_register_date.name:
        [
            '2022-01-01', '2022-01-01', '2022-04-01', '1990-01-01',
            '1990-01-01', '2022-01-01', '2022-03-01', '2022-03-01',
            '1990-01-01', '2022-03-01', '1990-01-01', '2022-04-01',
            '2022-04-01', '2022-04-01', '2022-04-01'
        ],
    TicketsWithIterations.tribes_ids.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None,
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None
        ],
    TicketsWithIterations.tribes_names.name:
        [
            'tribe1', 'tribe3', 'tribe3', 'tribe3', 'tribe3', 'tribe3',
            'tribe3', 'tribe1', 'tribe1', 'tribe1', 'tribe1', None, 'tribe1',
            'tribe1', None
        ],
    TicketsWithIterations.tent_id.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002'
        ],
    TicketsWithIterations.tent_name.name:
        [
            'tent1', 'tent2', 'tent2', 'tent2', 'tent1', 'tent2', 'tent3',
            'tent2', 'tent2', 'tent1', 'tent2', 'tent2', 'tent2', 'tent1',
            'tent2'
        ],
    TicketsWithIterations.ticket_id.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000005',
            '00000000-0000-0000-0000-000000000006',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000008',
            '00000000-0000-0000-0000-000000000009',
            '00000000-0000-0000-0000-000000000010',
            '00000000-0000-0000-0000-000000000011',
            '00000000-0000-0000-0000-000000000012',
            '00000000-0000-0000-0000-000000000013',
            '00000000-0000-0000-0000-000000000014',
            '00000000-0000-0000-0000-000000000015'
        ],
    TicketsWithIterations.ticket_id.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000003',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000005',
            '00000000-0000-0000-0000-000000000006',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000008',
            '00000000-0000-0000-0000-000000000009',
            '00000000-0000-0000-0000-000000000010',
            '00000000-0000-0000-0000-000000000011',
            '00000000-0000-0000-0000-000000000012',
            '00000000-0000-0000-0000-000000000013',
            '00000000-0000-0000-0000-000000000014',
            '00000000-0000-0000-0000-000000000015'
        ],
    TicketsWithIterations.ticket_scid.name:
        [
            'trial (11)', 'licensed (0)', 'assigned_to_someone (4)',
            'licensed (0)', 'revoked (3)', 'expired (2)', 'no license (5)',
            'licensed (0)', 'no_license_revoked (6)', 'no_license_expired (7)',
            'no_license_expired_revoked (8)', 'trial (11)',
            'no_license_free (9)', 'no_license_expired_free (10)', 'free (1)'
        ],
    TicketsWithIterations.ticket_type.name:
        [1, 1, 1, 1, 1, 1, 2, 6, 1, 2, 1, 1, 1, 1, 1],
    TicketsWithIterations.creation_date.name:
        [
            '2023-02-01', '2023-07-01', '2023-08-01', '2024-01-01',
            '2024-04-02', '2024-06-02', '2023-02-02', '2023-02-03',
            '2024-04-02', '2024-02-02', '2024-07-02', '2023-01-02',
            '2023-03-02', '2024-03-02', '2023-03-02'
        ],
    TicketsWithIterations.is_private.name: [True] * 15,
    TicketsWithIterations.user_groups.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None,
            '00000000-0000-0000-0000-000000000001;00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001;00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001;00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001;00000000-0000-0000-0000-000000000002',
            None, None, None, None
        ],
    TicketsWithIterations.ticket_tags.name:
        [
            '(00000000-0000-0000-0000-000000000001);(00000000-0000-0000-0000-000000000002)',
            '(00000000-0000-0000-0000-000000000001);(00000000-0000-0000-0000-000000000003)',
            '(00000000-0000-0000-0000-000000000003)',
            '(00000000-0000-0000-0000-000000000003)',
            '(00000000-0000-0000-0000-000000000003)', None, None, None, None,
            None, None, None, None, None, None
        ],
    TicketsWithIterations.platforms.name:
        [
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000004',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None,
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None, None, None, None,
            None, None, None
        ],
    TicketsWithIterations.products.name:
        [
            None, None, '00000000-0000-0000-0000-000000000006',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000007',
            '00000000-0000-0000-0000-000000000011',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001', None,
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000011'
        ],
    TicketsWithIterations.frameworks.name:
        [
            None, None, None, None, None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000001', None, None, None, None
        ],
    TicketsWithIterations.builds.name:
        [
            None, None, None, None, None, None, None, None, None, None, None,
            None, '00000000-0000-0000-0000-000000000001', None, None
        ],
    TicketsWithIterations.fixed_in_builds.name:
        [
            None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000007', None, None, None, None,
            None, None, None, None
        ],
    TicketsWithIterations.fixed_by.name:
        [
            None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000002', None, None, None, None,
            None, None, None, None
        ],
    TicketsWithIterations.fixed_on.name:
        [
            None, None, None, None, None, None, '2024-02-03', None, None, None,
            None, None, None, None, None
        ],
    TicketsWithIterations.ticket_status.name:
        [
            None, None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000011', None, None, None, None,
            None, None, None
        ],
    TicketsWithIterations.closed_by.name:
        [
            '00000000-0000-0000-0000-000000000001', None, None, None, None,
            None, None, None, None, None, None, None, None, None, None
        ],
    TicketsWithIterations.closed_on.name:
        [
            '2023-02-01', None, None, None, None, None, None, None, None, None,
            None, None, None, None, None
        ],
    TicketsWithIterations.severity.name:
        [
            None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000007', None, None, None, None,
            None, None, None, None
        ],
    TicketsWithIterations.converted_to_bug_on.name:
        [
            None, None, None, None, None, None, '2023-02-02', None, None, None,
            None, None, None, None, None
        ],
    TicketsWithIterations.duplicated_to_ticket_type.name:
        [
            None, None, None, None, None, None, None, None, None, 1, None,
            None, None, None, None
        ],
    TicketsWithIterations.duplicated_to_ticket_scid.name:
        [
            None, None, None, None, None, None, None, None, None, 'trial (11)',
            None, None, None, None, None
        ],
    TicketsWithIterations.assigned_to.name:
        [
            None, None, None, None, None, None, None, None,
            '00000000-0000-0000-0000-000000000001', None, None, None, None,
            None, None
        ],
    TicketsWithIterations.operating_system_id.name:
        [
            None, None, None, '00000000-0000-0000-0000-000000000007', None,
            None, None, None, None, None, None, None, None, None, None
        ],
    TicketsWithIterations.ide_id.name:
        [
            None, None, None, None, '00000000-0000-0000-0000-000000000007',
            None, None, None, None, None, None, None, None, None, None
        ],
    TicketsWithIterations.reply_id.name:
        [
            '00000000-0000-0000-0000-000000000001', None, None, None, None,
            None, None, None, None, None, None, None, None, None, None
        ],
    TicketsWithIterations.component_id.name:
        [
            None, '00000000-0000-0000-0000-000000000004', None, None, None,
            None, None, None, None, None, None, None, None, None, None
        ],
    TicketsWithIterations.feature_id.name:
        [
            None, None, '00000000-0000-0000-0000-000000000006', None, None,
            None, None, None, None, None, None, None, None, None, None
        ],
    TicketsWithIterations.license_name.name:
        [
            None, 'free bundle', 'dxp', 'dxp', 'dxp', 'dxp', None,
            'devextreme', None, None, None, None, None, None, 'devextreme'
        ],
    TicketsWithIterations.parent_license_name.name:
        [
            None, 'dxp', None, None, None, None, None, None, None, None, None,
            None, None, None, None
        ],
    TicketsWithIterations.subscription_start.name:
        [
            None, '2023-06-01', '2023-01-01', '2023-06-01', '2023-06-01',
            '2023-06-01', None, '2023-01-01', None, None, None, None, None,
            None, '2023-02-01'
        ],
    TicketsWithIterations.expiration_date.name:
        [
            None, '2024-05-31', '2024-01-01', '2024-05-31', '2024-05-31',
            '2024-05-31', None, '2024-01-01', None, None, None, None, None,
            None, '2024-02-01'
        ],
    TicketsWithIterations.license_status.name:
        [11, 0, 4, 0, 3, 2, 5, 0, 6, 7, 8, 11, 9, 10, 1],
    TicketsWithIterations.conversion_status.name:
        [
            0, 0, None, None, None, None, None, None, None, None, None, 1,
            None, None, 1
        ],
}

dtfields = (
    TicketsWithIterations.user_register_date.name,
    TicketsWithIterations.creation_date.name,
    TicketsWithIterations.fixed_on.name,
    TicketsWithIterations.closed_on.name,
    TicketsWithIterations.converted_to_bug_on.name,
    TicketsWithIterations.subscription_start.name,
    TicketsWithIterations.expiration_date.name,
)

params = {
    'years_of_history': 'YEAR, -35',
    'employees_json': '',
    'start_date': '2022-01-01',
    'end_date': '2025-01-01',
}
