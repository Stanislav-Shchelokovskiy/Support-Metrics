DROP TABLE IF EXISTS {Employees};
CREATE TABLE {Employees}(
  {position_id} TEXT,
  {tribe_id}    TEXT,
  {crmid}       TEXT PRIMARY KEY,
  {name}        TEXT
) WITHOUT ROWID;

INSERT INTO {Employees}
SELECT DISTINCT 
  {position_id},
  {tribe_id},
  {crmid},
  {name}
FROM {EmployeesIterations}
ORDER BY {tribe_id}, {name};

CREATE INDEX idx_{Employees}_{position_id} ON {Employees}({position_id}, {tribe_id}, {crmid}, {name});
CREATE INDEX idx_{Employees}_{tribe_id} ON {Employees}({tribe_id}, {crmid}, {name});