DROP TABLE IF EXISTS {EmpPositions};
CREATE TABLE IF NOT EXISTS {EmpPositions} (
  "{id}"   TEXT,
  "{name}" TEXT
);

INSERT INTO {EmpPositions}
SELECT DISTINCT {pos_id}, {pos_name}
FROM {EmployeesIterations}
ORDER BY {pos_name};