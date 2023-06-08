DROP TABLE IF EXISTS {EmpTents};
CREATE TABLE {EmpTents}(
  {id}    TEXT PRIMARY KEY, 
  {name}  TEXT
) WITHOUT ROWID;

INSERT INTO {EmpTents}
SELECT DISTINCT 
  {tent_id} AS {id},
  {tent_name} AS {name}
FROM {EmployeesIterations}
WHERE {tent_id} IS NOT NULL;