CREATE TABLE TicketsWithIterations (
        emp_post_id                     TEXT,
        emp_crmid                       TEXT,
        emp_scid                        TEXT,
        emp_tribe_id                    TEXT,
        emp_tent_id                     TEXT,
        emp_position_id                 TEXT,
        emp_name                        TEXT,
        emp_position_name               TEXT,
        emp_tribe_name                  TEXT,
        emp_tent_name                   TEXT,
        roles                           TEXT,
        post_timestamp                  TEXT,
        post_tribe_id                   TEXT,
        post_tent_id                    TEXT,
        post_reply_id                   TEXT,
        post_component_id               TEXT,
        post_feature_id                 TEXT,
        resolution_in_hours             INTEGER,
        lifetime_in_hours               INTEGER,
        user_crmid                      TEXT,
        user_id                         TEXT,
        is_employee                     INTEGER,
        user_register_date              TEXT,
        ticket_id                       TEXT,
        ticket_scid                     TEXT,
        ticket_type                     INTEGER,
        tribes_ids                      TEXT,
        tribes_names                    TEXT,
        tent_id                         TEXT,
        tent_name                       TEXT,
        creation_date                   TEXT,
        is_private                      INTEGER,
        user_groups                     TEXT,
        ticket_tags                     TEXT,
        platforms                       TEXT,
        products                        TEXT,
        frameworks                      TEXT,
        builds                          TEXT,
        fixed_in_builds                 TEXT,
        fixed_by                        TEXT,
        fixed_on                        TEXT,
        ticket_status                   TEXT,
        closed_by                       TEXT,
        closed_on                       TEXT,
        severity                        TEXT,
        converted_to_bug_on             TEXT,
        duplicated_to_ticket_type       INTEGER,
        duplicated_to_ticket_scid       TEXT,
        assigned_to                     TEXT,
        operating_system_id             TEXT,
        ide_id                          TEXT,
        reply_id                        TEXT,
        component_id                    TEXT,
        feature_id                      TEXT,
        license_name                    TEXT,
        parent_license_name             TEXT,
        subscription_start              TEXT,
        expiration_date                 TEXT,
        license_status                  INTEGER,
        conversion_status               INTEGER
);
INSERT INTO TicketsWithIterations (emp_post_id, emp_crmid, emp_scid, emp_tribe_id, emp_tent_id, emp_position_id, emp_name, emp_position_name, emp_tribe_name, emp_tent_name, roles,                     post_timestamp,           post_tribe_id, post_tent_id, post_reply_id, post_component_id, post_feature_id, resolution_in_hours, lifetime_in_hours, user_crmid, user_id, is_employee, user_register_date, ticket_id, ticket_scid, ticket_type, tribes_ids,     tribes_names,   tent_id, tent_name, creation_date, is_private, user_groups, ticket_tags, platforms,            products,   frameworks,   builds,  fixed_in_builds, fixed_on, fixed_by, ticket_status, closed_by, closed_on,   severity, converted_to_bug_on, duplicated_to_ticket_type, duplicated_to_ticket_scid, assigned_to, operating_system_id, ide_id, reply_id, component_id, feature_id, license_name, parent_license_name, subscription_start, expiration_date, license_status, conversion_status)
VALUES                            ('1',         'e1',      'e1',     'tribe1',     'tent1',    'pos1',           'emp1',   'Support',        'Tribe1',        'Tent1',      'viewer;processor;employee','2023-04-11T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             20,                  50,                'u1',       'u_1',   0,           '2021-11-03',       't1',      't_1',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-04-11',  1,          'ug1',       'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-04-11',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('2',         'e2',      'e2',     'tribe1',     'tent2',    'pos2',           'emp2',   'Support',        'Tribe1',        'Tent1',      'viewer;employee',          '2023-05-21T19:28:39.713','tribe1',      'tent1',      '2',           '1',               '1',             20,                  50,                'u1',       'u_1',   0,           '2021-11-03',       't1',      't_1',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-05-21',  1,          'ug1;ug3',   'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-05-21',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'DXperience', NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('3',         'e3',      'e3',     'tribe1',     'tent3',    'pos3',           'emp2',   'Support',        'Tribe1',        'Tent1',      'processor;employee',       '2023-06-17T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             43,                  941,               'u2',       'u_2',   0,           '2021-11-03',       't2',      't_2',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-06-17',  1,          'ug1;ug2',   'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-06-17',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('4',         'e1',      'e1',     'tribe1',     'tent1',    'pos1',           'emp1',   'Support',        'Tribe1',        'Tent1',      'viewer;processor;employee','2023-07-10T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             43,                  941,               'u2',       'u_2',   0,           '2021-11-03',       't2',      't_2',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-07-10',  1,          'ug1;ug2',   'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-07-10',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('5',         'e2',      'e2',     'tribe1',     'tent2',    'pos2',           'emp2',   'Support',        'Tribe1',        'Tent1',      'viewer;employee',          '2023-08-02T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             123,                 832,               'u3',       'u_3',   0,           '2021-11-03',       't3',      't_3',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-08-02',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-08-02',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('6',         'e3',      'e3',     'tribe1',     'tent3',    'pos3',           'emp3',   'Support',        'Tribe1',        'Tent1',      'processor;employee',       '2023-09-03T19:28:39.713','tribe1',      'tent1',      '2',           '1',               '1',             123,                 832,               'u4',       'u_4',   0,           '2021-11-03',       't3',      't_3',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-09-03',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-09-03',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('7',         'e1',      'e1',     'tribe1',     'tent1',    'pos1',           'emp1',   'Support',        'Tribe1',        'Tent1',      'viewer;processor;employee','2023-10-07T19:28:39.713','tribe1',      'tent1',      '3',           '1',               '1',             53,                  941,               'u5',       'u_5',   0,           '2021-11-03',       't4',      't_4',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-10-07',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-10-07',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('8',         'e2',      'e2',     'tribe1',     'tent2',    'pos2',           'emp2',   'Support',        'Tribe1',        'Tent1',      'viewer;employee',          '2023-11-19T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             4,                   41,                'u6',       'u_6',   0,           '2021-11-03',       't5',      't_5',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-11-19',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-11-19',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('9',         'e3',      'e3',     'tribe1',     'tent3',    'pos3',           'emp3',   'Support',        'Tribe1',        'Tent1',      'processor;employee',       '2023-12-03T19:28:39.713','tribe1',      'tent1',      '4',           '1',               '1',             3,                   91,                'u7',       'u_7',   0,           '2021-11-03',       't6',      't_6',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2023-12-03',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2023-12-03',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('10',        'e1',      'e1',     'tribe1',     'tent1',    'pos1',           'emp1',   'Support',        'Tribe1',        'Tent1',      'viewer;processor;employee','2024-01-01T19:28:39.713','tribe1',      'tent1',      '2',           '1',               '1',             143,                 241,               'u8',       'u_8',   0,           '2021-11-03',       't7',      't_7',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2024-01-01',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2024-01-01',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('11',        'e2',      'e2',     'tribe1',     'tent2',    'pos2',           'emp2',   'Support',        'Tribe1',        'Tent1',      'viewer;employee',          '2024-02-02T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             423,                 521,               'u9',       'u_9',   0,           '2021-11-03',       't8',      't_8',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2024-02-02',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2024-02-02',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('12',        'e3',      'e3',     'tribe1',     'tent3',    'pos3',           'emp3',   'Support',        'Tribe1',        'Tent1',      'processor;employee',       '2024-03-04T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             72,                  82,                'u8',       'u_8',   0,           '2021-11-03',       't9',      't_9',       1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2024-03-04',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2024-03-04',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('13',        'e1',      'e1',     'tribe1',     'tent1',    'pos1',           'emp1',   'Support',        'Tribe1',        'Tent1',      'viewer;processor;employee','2024-04-03T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             94,                  98,                'u7',       'u_7',   0,           '2021-11-03',       't10',     't_10',      1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2024-04-03',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2024-04-03',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             ),
                                  ('14',        'e1',      'e1',     'tribe1',     'tent1',    'pos1',           'emp1',   'Support',        'Tribe1',        'Tent1',      'viewer;processor;employee','2024-05-02T19:28:39.713','tribe1',      'tent1',      '1',           '1',               '1',             99,                  101,               'u6',       'u_6',   0,           '2021-11-03',       't11',     't_11',      1,           'tribe1;tribe2','Tribe1;Tribe2','tent1', 'Tent1',   '2024-05-02',  1,          NULL,        'tag1;tag2','platform1;platform2', 'product1', 'framework1', '23.2.4',NULL,            NULL,     NULL,     'Closed',      'e1',      '2024-05-02',NULL,     NULL,                NULL,                      NULL,                      NULL,        'os1',               'ide1', '1',      '1',          '1',        'Universal',  NULL,                '2023-08-15',       '2024-08-15',    0,              NULL             );
CREATE UNIQUE INDEX idx_TicketsWithIterations_unique_cols ON TicketsWithIterations(user_crmid, ticket_scid, emp_post_id);
CREATE INDEX idx_TicketsWithIterations_tickets_inner ON TicketsWithIterations(user_crmid, ticket_scid, creation_date, ticket_type, license_status, emp_position_id, is_private, tribes_ids, tent_id);
CREATE INDEX idx_TicketsWithIterations_iterations_inner ON TicketsWithIterations(user_crmid, emp_post_id, creation_date, ticket_type, license_status, emp_position_id, is_private, tribes_ids, tent_id);
CREATE INDEX idx_TicketsWithIterations_outer ON TicketsWithIterations(user_crmid, creation_date, ticket_type, license_status, emp_position_id, is_private, tribes_ids, tent_id, user_id, ticket_scid, emp_post_id);


CREATE TABLE CSI (
        ticket_scid TEXT,
        date TEXT,
        rating INTEGER,
        PRIMARY KEY (
                ticket_scid,
                date,
                rating
        )
) WITHOUT ROWID;
INSERT INTO CSI VALUES('t_1','2023-05-15',  -1);
INSERT INTO CSI VALUES('t_2','2023-06-21',  0 );
INSERT INTO CSI VALUES('t_3','2023-07-13',  1 );
INSERT INTO CSI VALUES('t_4','2023-08-30',  -1);
INSERT INTO CSI VALUES('t_5','2023-09-10',  0 );
INSERT INTO CSI VALUES('t_6','2023-10-04',  1 );
INSERT INTO CSI VALUES('t_7','2023-11-17',  -1);
INSERT INTO CSI VALUES('t_8','2023-12-16',  0 );
INSERT INTO CSI VALUES('t_9','2024-01-11',  1 );
INSERT INTO CSI VALUES('t_10','2024-02-18', -1);
INSERT INTO CSI VALUES('t_11','2024-03-02', 0 );
INSERT INTO CSI VALUES('t_12','2023-04-20', 1 );
INSERT INTO CSI VALUES('t_13','2024-05-01', 1 );


CREATE TABLE CustomersGroups (
        id TEXT,
        name TEXT,
        creation_date TEXT,
        PRIMARY KEY (
                id
        )
) WITHOUT ROWID;

INSERT INTO CustomersGroups VALUES('ug1','Ug1',  '2023-01-15');
INSERT INTO CustomersGroups VALUES('ug2','Ug2',  '2023-02-15');
INSERT INTO CustomersGroups VALUES('ug3','Ug3',  '2023-03-15');

CREATE TABLE TrackedCustomersGroups (
        user_crmid TEXT,
        id TEXT,
        name TEXT,
        assignment_date TEXT,
        removal_date TEXT,
        PRIMARY KEY (
                user_crmid,
                id
        )
) WITHOUT ROWID;

INSERT INTO TrackedCustomersGroups VALUES('u1','ug1', 'Ug1', '2022-01-15', NULL);
INSERT INTO TrackedCustomersGroups VALUES('u1','ug3', 'Ug3', '2022-05-05', NULL);
INSERT INTO TrackedCustomersGroups VALUES('u2','ug1', 'Ug1', '2023-06-02', NULL);
INSERT INTO TrackedCustomersGroups VALUES('u2','ug2', 'Ug2', '2023-05-02', NULL);
