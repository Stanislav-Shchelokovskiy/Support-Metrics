DROP TABLE IF EXISTS {TicketsWithIterations};
CREATE TABLE IF NOT EXISTS {TicketsWithIterations} (
  "{user_id}"            TEXT,
  "{tribe_id}"           TEXT,
  "{tribe_name}"         TEXT,
  "{ticket_id}"          TEXT,
  "{ticket_scid}"        TEXT,
  "{ticket_type}"        INTEGER,
  "{creation_date}"      DATE,
  "{user_groups}"        TEXT,
  "{ticket_tags}"        TEXT,
  "{platforms}"          TEXT,
  "{products}"           TEXT,
  "{reply_id}"           TEXT,
  "{component_id}"       TEXT,
  "{feature_id}"         TEXT,
  "{license_status}"     INTEGER,
  "{conversion_status}"  INTEGER,
  "{emp_post_id}"        TEXT,
  "{emp_scid}"           TEXT,
  "{emp_crmid}"          TEXT,
  "{emp_tribe_id}"       TEXT,
  "{emp_pos_id}"         TEXT,
  "{emp_name}"           TEXT,
  "{emp_pos_name}"       TEXT,
  "{emp_tribe_name}"     TEXT
);

INSERT INTO {TicketsWithIterations}
SELECT
    t.{user_id},
    t.{tribe_id},
    t.{tribe_name},
    t.{ticket_id},
    t.{ticket_scid},
    t.{ticket_type},
    t.{creation_date},
    t.{user_groups},
    t.{ticket_tags},
    t.{platforms},
    t.{products},
    t.{reply_id},
    t.{component_id},
    t.{feature_id},
    t.{license_status},
    t.{conversion_status},
    ei.{post_id}    AS emp_post_id,
    ei.{scid}       AS emp_scid,
    ei.{crmid}      AS emp_crmid,
    ei.{tribe_id}   AS emp_tribe_id,
    ei.{pos_id}     AS emp_pos_id,
    ei.{name}       AS emp_name,
    ei.{pos_name}   AS emp_pos_name,
    ei.{tribe_name} AS emp_tribe_name
FROM
    {TicketsWithLicenses} AS t
    LEFT JOIN {EmployeesIterations} AS ei ON ei.{ticket_id} = t.{ticket_id};

CREATE INDEX idx_{TicketsWithIterations}_{creation_date} ON {TicketsWithIterations}({creation_date}, {tribe_id}, {emp_pos_id});
