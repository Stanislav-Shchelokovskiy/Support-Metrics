DECLARE @licensed		TINYINT = 0
DECLARE @expired		TINYINT = 1
DECLARE @revoked		TINYINT = 2
DECLARE @free			TINYINT = 3
DECLARE @trial			TINYINT = 4
DECLARE @converted_paid	TINYINT = 5
DECLARE @converted_free	TINYINT = 6


SELECT
	{user_id},
	{tribe_id},
	{tribe_name},
	{scid},
	{ticket_type},
	{creation_date},
	{iterations},
	{user_groups},
	{ticket_tags},
	{platform_ids},
	{product_ids},
	{reply_id},
	{component_id},
	{feature_id},
	{license_status},
	IIF(trial_user_id IS NOT NULL, 
		IIF(license_status = @licensed, @converted_paid, 
			IIF(license_status = @free,  @converted_free, NULL)), 
				NULL) AS {conversion_status}
FROM 
	#TicketsWithIterationsAndLicenses AS ti
	OUTER APPLY (SELECT DISTINCT user_id AS trial_user_id
				 FROM	#TicketsWithIterationsAndLicenses
				 WHERE	user_id = ti.user_id AND
						license_status = @trial) AS ti_trial