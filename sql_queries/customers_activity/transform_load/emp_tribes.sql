DROP TABLE IF EXISTS {EmpTribes};
CREATE TABLE {EmpTribes} AS
SELECT DISTINCT 
  {tribe_id} AS {id},
  {tribe_name} AS {name}
FROM {EmployeesIterations}
WHERE {tribe_id} IS NOT NULL
ORDER BY {name};