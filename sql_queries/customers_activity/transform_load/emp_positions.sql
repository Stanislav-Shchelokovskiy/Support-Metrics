DROP TABLE IF EXISTS {EmpPositions};
CREATE TABLE {EmpPositions} (
  "{id}"   TEXT,
  "{name}" TEXT
);

INSERT INTO {EmpPositions}
SELECT DISTINCT {position_id}, {position_name}
FROM {EmployeesIterations}
ORDER BY {position_name};