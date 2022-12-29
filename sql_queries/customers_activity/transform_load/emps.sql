DROP TABLE IF EXISTS {Employees};
CREATE TABLE IF NOT EXISTS {Employees} (
  "{pos_id}"   TEXT,
  "{tribe_id}" TEXT,
  "{name}" TEXT
);

INSERT INTO {Employees}
SELECT DISTINCT {pos_id}, {tribe_id}, {name}
FROM {EmployeesIterations};

CREATE INDEX idx_{Employees}_{pos_id} ON {Employees}({pos_id}, {tribe_id}, {name});
CREATE INDEX idx_{Employees}_{tribe_id} ON {Employees}({tribe_id}, {name});