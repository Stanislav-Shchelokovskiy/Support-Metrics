group_by = '%Y-%W'
start = '2023-05-01'
end = '2024-06-01'
baseline_aligned_mode_enabled = False
metric = 'Ticket Lifetime'
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
    'Resolution time': {
        'include': True,
        'values': [1, 430]
    },
    'Roles': {
        'include': True,
        'values': ['viewer', 'processor', 'employee']
    }
}
