SELECT
	Id   						AS {id},
	Name 						AS {name},
	CAST(CreationDate AS DATE) 	AS {creation_date}
FROM CRM.dbo.UserGroups