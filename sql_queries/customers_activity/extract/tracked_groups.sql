DECLARE @start_date DATE = '{start_date}'

DECLARE @max_date DATE = '9999-12-31'
DECLARE @insert SMALLINT = 0
DECLARE @delete SMALLINT = 2

SELECT
	assigned_ug.Customer_Id AS {user_crmid},
	g.id	                AS {id},
	g.Name	                AS {name},
	assigned_ug.group_assign_date   AS {assignment_date},
	ISNULL(deleted_ug.group_removal_date, @max_date) AS {removal_date},
	DATEDIFF(DAY, MIN(assigned_ug.group_assign_date) OVER (PARTITION BY g.id), assigned_ug.group_assign_date) AS {offset_in_days}
FROM (	SELECT	Id AS id, Name AS name
		FROM	CRM.dbo.UserGroups
		WHERE	Name LIKE '% MAU %' AND Name NOT LIKE '% MAU | Candidate' ) AS g
	CROSS APPLY (	
		SELECT	Customer_Id,
				MAX(CONVERT(DATE, EntityModified)) AS group_assign_date
		FROM	CRMAudit.dxcrm.Customer_UserGroup
		WHERE	EntityModified > @start_date AND
				UserGroup_Id = g.id AND
				AuditAction = @insert
		GROUP BY Customer_Id,
				 UserGroup_Id ) AS assigned_ug
	OUTER APPLY (
		SELECT	MAX(CONVERT(DATE, EntityModified)) AS group_removal_date
		FROM	CRMAudit.dxcrm.Customer_UserGroup
		WHERE	EntityModified > @start_date AND
				UserGroup_Id = g.id AND
				AuditAction = @delete AND
				Customer_Id = assigned_ug.Customer_Id
		GROUP BY Customer_Id,
				 UserGroup_Id ) AS deleted_ug