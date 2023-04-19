DROP TABLE IF EXISTS {Employees};
CREATE TABLE {Employees}(
  {position_id}   TEXT,
  {tribe_id}      TEXT,
  {tent_id}       TEXT,
  {crmid}         TEXT PRIMARY KEY,
  {name}          TEXT,
  {tribe_name}    TEXT,
  {tent_name}     TEXT,
  {position_name} TEXT
) WITHOUT ROWID;

CREATE INDEX idx_{Employees}_{position_id}_{tribe_id} ON {Employees}({position_id}, {tribe_id}, {crmid}, {name});
CREATE INDEX idx_{Employees}_{tribe_id} ON {Employees}({tribe_id}, {crmid}, {name});

CREATE INDEX idx_{Employees}_{position_id}_{tent_id} ON {Employees}({position_id}, {tent_id}, {crmid}, {name});
CREATE INDEX idx_{Employees}_{tent_id} ON {Employees}({tent_id}, {crmid}, {name});
