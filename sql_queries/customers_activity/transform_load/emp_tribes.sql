DROP TABLE IF EXISTS {EmpTribes};
CREATE TABLE {EmpTribes} (
  "{id}"   TEXT,
  "{name}" TEXT
);

INSERT INTO {EmpTribes}
SELECT DISTINCT {tribe_id}, {tribe_name}
FROM {EmployeesIterations}
WHERE {tribe_id} IS NOT NULL
ORDER BY {tribe_name};