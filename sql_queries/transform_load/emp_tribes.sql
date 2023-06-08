DROP TABLE IF EXISTS {EmpTribes};
CREATE TABLE {EmpTribes}(
  {id}    TEXT PRIMARY KEY, 
  {name}  TEXT
) WITHOUT ROWID;

INSERT INTO {EmpTribes}
SELECT DISTINCT 
  {tribe_id} AS {id},
  {tribe_name} AS {name}
FROM {EmployeesIterations}
WHERE {tribe_id} IS NOT NULL;