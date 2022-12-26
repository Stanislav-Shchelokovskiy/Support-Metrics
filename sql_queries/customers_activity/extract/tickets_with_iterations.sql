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
	{platforms},
	{products},
	{reply_id},
	{component_id},
	{feature_id},
	{license_status},
	IIF(EXISTS(SELECT TOP 1 user_id
			   FROM #TicketsWithIterationsAndLicenses
			   WHERE user_id = ti.user_id AND license_status = @trial), 
		IIF(license_status = @licensed, @converted_paid, 
			IIF(license_status = @free,  @converted_free,
				IIF(license_status = @trial, 
					IIF(EXISTS(SELECT TOP 1 user_id
							   FROM #TicketsWithIterationsAndLicenses
							   WHERE user_id = ti.user_id AND license_status = @licensed), @converted_paid,
						IIF(EXISTS(SELECT TOP 1 user_id
								   FROM #TicketsWithIterationsAndLicenses
								   WHERE user_id = ti.user_id AND license_status = @free), @converted_free, 
						NULL)
					),
				NULL)
			)
		), 
	NULL) AS {conversion_status},
	{emp_post_id},
	{emp_name},
	{emp_pos_name},
	{emp_tribe_name},
	{emp_crmid},
	{emp_pos_id},
	{emp_tribe_id}
FROM 
	#TicketsWithIterationsAndLicenses AS ti