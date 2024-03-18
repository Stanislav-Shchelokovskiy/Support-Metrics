-- backup
CREATE TABLE IF NOT EXISTS TicketsWithIterationsBACKUP AS SELECT * FROM TicketsWithIterations;

-- create intermediate
DROP TABLE IF EXISTS TicketsWithIterationsTEMP;
CREATE TABLE TicketsWithIterationsTEMP AS SELECT * FROM TicketsWithIterationsBACKUP;

-- alter intermediate
ALTER TABLE TicketsWithIterationsTEMP ADD COLUMN post_tribe_id      TEXT;
ALTER TABLE TicketsWithIterationsTEMP ADD COLUMN post_tent_id       TEXT;
ALTER TABLE TicketsWithIterationsTEMP ADD COLUMN post_reply_id      TEXT;
ALTER TABLE TicketsWithIterationsTEMP ADD COLUMN post_component_id  TEXT;
ALTER TABLE TicketsWithIterationsTEMP ADD COLUMN post_feature_id    TEXT;

-- update intermediate
UPDATE  TicketsWithIterationsTEMP AS ti
SET     post_tribe_id = i.post_tribe_id,
        post_tent_id = i.post_tent_id,
        post_reply_id = i.post_reply_id,
        post_component_id = i.post_component_id,
        post_feature_id = i.post_feature_id
FROM    EmployeesIterations AS i
WHERE   i.ticket_id = ti.ticket_id AND i.post_id = ti.emp_post_id;

-- update original
DROP TABLE IF EXISTS TicketsWithIterations;
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

INSERT INTO TicketsWithIterations
SELECT DISTINCT
        emp_post_id                     AS emp_post_id,
        emp_crmid                       AS emp_crmid,
        emp_scid                        AS emp_scid,
        emp_tribe_id                    AS emp_tribe_id,
        emp_tent_id                     AS emp_tent_id,
        emp_position_id                 AS emp_position_id,
        emp_name                        AS emp_name,
        emp_position_name               AS emp_position_name,
        emp_tribe_name                  AS emp_tribe_name,
        emp_tent_name                   AS emp_tent_name,
        roles                           AS roles,
        post_tribe_id                   AS post_tribe_id,
        post_tent_id                    AS post_tent_id,
        post_reply_id                   AS post_reply_id,
        post_component_id               AS post_component_id,
        post_feature_id                 AS post_feature_id,
        resolution_in_hours             AS resolution_in_hours,
        lifetime_in_hours               AS lifetime_in_hours,
        user_crmid                      AS user_crmid,
        user_id                         AS user_id,
        is_employee                     AS is_employee,
        user_register_date              AS user_register_date,
        ticket_id                       AS ticket_id,
        ticket_scid                     AS ticket_scid,
        ticket_type                     AS ticket_type,
        tribes_ids                      AS tribes_ids,
        tribes_names                    AS tribes_names,
        tent_id                         AS tent_id,
        tent_name                       AS tent_name,
        creation_date                   AS creation_date,
        is_private                      AS is_private,
        user_groups                     AS user_groups,
        ticket_tags                     AS ticket_tags,
        platforms                       AS platforms,
        products                        AS products,
        frameworks                      AS frameworks,
        builds                          AS builds,
        fixed_in_builds                 AS fixed_in_builds,
        fixed_by                        AS fixed_by,
        fixed_on                        AS fixed_on,
        ticket_status                   AS ticket_status,
        closed_by                       AS closed_by,
        closed_on                       AS closed_on,
        severity                        AS severity,
        converted_to_bug_on             AS converted_to_bug_on,
        duplicated_to_ticket_type       AS duplicated_to_ticket_type,
        duplicated_to_ticket_scid       AS duplicated_to_ticket_scid,
        assigned_to                     AS assigned_to,
        operating_system_id             AS operating_system_id,
        ide_id                          AS ide_id,
        reply_id                        AS reply_id,
        component_id                    AS component_id,
        feature_id                      AS feature_id,
        license_name                    AS license_name,
        parent_license_name             AS parent_license_name,
        subscription_start              AS subscription_start,
        expiration_date                 AS expiration_date,
        license_status                  AS license_status,
        conversion_status               AS conversion_status
FROM    TicketsWithIterationsTEMP
-- WHERE   user_crmid IS NOT NULL AND
--         ticket_scid IS NOT NULL AND
        --emp_post_id IS NOT NULL

/*
ON CONFLICT(user_crmid, ticket_scid, emp_post_id) DO UPDATE SET
        --emp_post_id
        emp_crmid                       = excluded.emp_crmid,
        emp_scid                        = excluded.emp_scid,
        emp_tribe_id                    = excluded.emp_tribe_id,
        emp_tent_id                     = excluded.emp_tent_id,
        emp_position_id                 = excluded.emp_position_id,
        emp_name                        = excluded.emp_name,
        emp_position_name               = excluded.emp_position_name,
        emp_tribe_name                  = excluded.emp_tribe_name,
        emp_tent_name                   = excluded.emp_tent_name,
        roles                           = excluded.roles,
        post_tribe_id                   = excluded.post_tribe_id,
        post_tent_id                    = excluded.post_tent_id,
        post_reply_id                   = excluded.post_reply_id,
        post_component_id               = excluded.post_component_id,
        post_feature_id                 = excluded.post_feature_id
        resolution_in_hours             = excluded.resolution_in_hours,
        lifetime_in_hours               = excluded.lifetime_in_hours,
        --user_crmid
        user_id                         = excluded.user_id,
        is_employee                     = excluded.is_employee,
        user_register_date              = excluded.user_register_date,
        ticket_id                       = excluded.ticket_id,
        --ticket_scid
        ticket_type                     = excluded.ticket_type,
        tribes_ids                      = excluded.tribes_ids,
        tribes_names                    = excluded.tribes_names,
        tent_id                         = excluded.tent_id,
        tent_name                       = excluded.tent_name,
        creation_date                   = excluded.creation_date,
        is_private                      = excluded.is_private,
        user_groups                     = excluded.user_groups,
        ticket_tags                     = excluded.ticket_tags,
        platforms                       = excluded.platforms,
        products                        = excluded.products,
        frameworks                      = excluded.frameworks,
        builds                          = excluded.builds,
        fixed_in_builds                 = excluded.fixed_in_builds,
        fixed_by                        = excluded.fixed_by,
        fixed_on                        = excluded.fixed_on,
        ticket_status                   = excluded.ticket_status,
        closed_by                       = excluded.closed_by,
        closed_on                       = excluded.closed_on,
        severity                        = excluded.severity,
        converted_to_bug_on             = excluded.converted_to_bug_on,
        duplicated_to_ticket_type       = excluded.duplicated_to_ticket_type,
        duplicated_to_ticket_scid       = excluded.duplicated_to_ticket_scid,
        assigned_to                     = excluded.assigned_to,
        operating_system_id             = excluded.operating_system_id,
        ide_id                          = excluded.ide_id,
        reply_id                        = excluded.reply_id,
        component_id                    = excluded.component_id,
        feature_id                      = excluded.feature_id,
        license_name                    = excluded.license_name,
        parent_license_name             = excluded.parent_license_name,
        subscription_start              = excluded.subscription_start,
        expiration_date                 = excluded.expiration_date,
        license_status                  = excluded.license_status,
        conversion_status               = excluded.conversion_status;
*/
;

CREATE UNIQUE INDEX idx_TicketsWithIterations_unique_cols ON TicketsWithIterations(user_crmid, ticket_scid, emp_post_id);
CREATE INDEX idx_TicketsWithIterations_tickets_inner ON TicketsWithIterations(user_crmid, ticket_scid, creation_date, ticket_type, license_status, emp_position_id, is_private, tribes_ids, tent_id);
CREATE INDEX idx_TicketsWithIterations_iterations_inner ON TicketsWithIterations(user_crmid, emp_post_id, creation_date, ticket_type, license_status, emp_position_id, is_private, tribes_ids, tent_id);
CREATE INDEX idx_TicketsWithIterations_outer ON TicketsWithIterations(user_crmid, creation_date, ticket_type, license_status, emp_position_id, is_private, tribes_ids, tent_id, user_id, ticket_scid, emp_post_id);

DROP TABLE TicketsWithIterationsTEMP;
