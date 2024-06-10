group_by = '%Y-%Q'
start = '2023-05-01'
end = '2024-06-01'
baseline_aligned_mode_enabled = False
metric = 'Iterations / Tickets'
body = {
    'Percentile':
        {
            'metric': 'iterations',
            'value': {
                'include': True,
                'value': 80
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
    'Roles': {
        'include': True,
        'values': ['viewer', 'processor', 'employee']
    }
}
