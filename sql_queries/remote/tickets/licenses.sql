DECLARE @actual_lic_origin     TINYINT = 0
DECLARE @historical_lic_origin TINYINT = 1

DROP TABLE IF EXISTS #LisencesOnly
SELECT	*
INTO	#LisencesOnly
FROM (	SELECT	Id					AS id,
				Owner_Id			AS owner_crmid,
				EndUser_Id			AS end_user_crmid,
				OrderItem_Id		AS order_item_id,
				@actual_lic_origin	AS lic_origin,
				NULL				AS revoked_since
		FROM	CRM.dbo.Licenses
		UNION
		SELECT	EntityOid,
				Owner_Id,
				EndUser_Id,
				OrderItem_Id,
				@historical_lic_origin,
				IIF(ChangedProperties LIKE '%EndUser%', CONVERT(DATE, EntityModified), NULL)
		FROM 	CRMAudit.dxcrm.Licenses
) AS l
