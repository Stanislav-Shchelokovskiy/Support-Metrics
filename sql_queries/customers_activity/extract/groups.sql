SELECT
	Id   												AS {id},
	Name 												AS {name},
	CAST(ISNULL(CreationDate, '1990-01-01') AS DATE) 	AS {creation_date}
FROM CRM.dbo.UserGroups