DROP TABLE IF EXISTS {EmpPositions};
CREATE TABLE {EmpPositions}(
  {id}    TEXT PRIMARY KEY, 
  {name}  TEXT
) WITHOUT ROWID;

INSERT INTO {EmpPositions}
SELECT DISTINCT
  {position_id} AS {id}, 
  {position_name} AS {name}
FROM {EmployeesIterations};