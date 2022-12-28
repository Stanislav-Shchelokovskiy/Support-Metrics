DROP TABLE IF EXISTS #TicketsWithLicenses
CREATE TABLE #TicketsWithLicenses (
	user_crmid		UNIQUEIDENTIFIER,
	user_id			NVARCHAR(20),
	tribe_id		UNIQUEIDENTIFIER,
	tribe_name		NVARCHAR(100),
	ticket_id		UNIQUEIDENTIFIER,
	ticket_scid		NVARCHAR(20),
	ticket_type		TINYINT,
	creation_date	DATE,
	user_groups		NVARCHAR(MAX),
	ticket_tags		NVARCHAR(MAX),
	platforms		NVARCHAR(MAX),
	products		NVARCHAR(MAX),
	reply_id		UNIQUEIDENTIFIER,
	component_id	UNIQUEIDENTIFIER,
	feature_id		UNIQUEIDENTIFIER,
	license_status  TINYINT
)

DROP INDEX IF EXISTS idx_user_id ON #TicketsWithLicenses
CREATE NONCLUSTERED INDEX idx_user_id ON #TicketsWithLicenses(user_id, license_status)