DROP TABLE IF EXISTS {EmpPositions};
CREATE TABLE {EmpPositions} AS
SELECT DISTINCT
  {position_id} AS {id}, 
  {position_name} AS {name}
FROM {EmployeesIterations}
ORDER BY {name};