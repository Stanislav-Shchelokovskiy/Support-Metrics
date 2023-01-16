DROP TABLE IF EXISTS {Employees};
CREATE TABLE {Employees} AS
SELECT DISTINCT 
  {position_id},
  {tribe_id},
  {crmid},
  {name}
FROM {EmployeesIterations}
ORDER BY {tribe_id}, {name};

CREATE INDEX idx_{Employees}_{position_id} ON {Employees}({position_id}, {tribe_id});
CREATE INDEX idx_{Employees}_{tribe_id} ON {Employees}({tribe_id});