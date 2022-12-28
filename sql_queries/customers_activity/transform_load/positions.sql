DROP TABLE IF EXISTS {Positions};
CREATE TABLE IF NOT EXISTS {Positions} (
  "{id}"   TEXT,
  "{name}" TEXT
);

INSERT INTO {Positions}
SELECT DISTINCT {pos_id}, {pos_name}
FROM {EmployeesIterations}
ORDER BY {pos_name};