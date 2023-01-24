DROP TABLE IF EXISTS {Users};
CREATE TABLE {Users}(
  {id}    TEXT PRIMARY KEY, 
  {name}  TEXT
) WITHOUT ROWID;

INSERT INTO {Users}
SELECT DISTINCT 
    user_crmid  AS {id}, 
    user_id     AS {name}
FROM {TicketsWithIterations};