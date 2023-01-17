DROP TABLE IF EXISTS {Users};
CREATE TABLE {Users} AS
SELECT DISTINCT 
    {user_crmid} AS {id}, 
    {user_id} AS {name}
FROM {TicketsWithLicenses};

CREATE INDEX idx_{Users}_{id} ON {Users}({id},{name});