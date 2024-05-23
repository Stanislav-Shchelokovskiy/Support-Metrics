group_by = '%Y-%Q'
start = '2023-05-01'
end = '2024-06-01'
baseline_aligned_mode_enabled = True
metric = 'Tickets'
body = {
    'Percentile':
        {
            'metric': 'iterations',
            'value': {
                'include': True,
                'value': 100
            }
        },
    'Ticket owner': {
        'include': True,
        'value': 0
    },
    'Ticket visibility': {
        'include': False,
        'value': 0
    },
    'User Groups': {
        'include': True,
        'values': ['ug1']
    },
    'Roles': {
        'include': True,
        'values': ['viewer', 'processor', 'employee']
    }
}
