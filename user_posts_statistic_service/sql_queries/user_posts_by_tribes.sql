-- USE DXStatisticsV2
DECLARE @licensed  TINYINT = 0
DECLARE @expired TINYINT = 1
DECLARE @revoked TINYINT = 2
DECLARE @trial   TINYINT = 3

DECLARE @actual_lic_origin  TINYINT = 0
DECLARE @historical_lic_origin TINYINT = 1

DECLARE @current_date DATE = CAST(GETUTCDATE() AS DATE)
DECLARE @period_start DATE = DATEADD(YEAR, -1, @current_date)
DECLARE @period_end DATE = DATEADD(DAY, 1, @current_date);

WITH licenses AS (
	SELECT
		Owner_Id AS owner_id,
		EndUser_Id AS end_user_id,
		OrderItem_Id AS order_item_id,
		@actual_lic_origin AS lic_origin,
		NULL AS revoked_since
	FROM
		CRM.dbo.Licenses
	UNION
	SELECT
		Owner_Id,
		EndUser_Id,
		OrderItem_Id,
		@historical_lic_origin,
		CONVERT(DATE,EntityModified)
	FROM 
		CRMAudit.dxcrm.Licenses
),

licenses_with_periods AS (
	SELECT
		l.owner_id,
		l.end_user_id,
		oi.SubscriptionStart AS subscription_start,
		DATEADD(DAY, ISNULL(oi.HoldingPeriod, 99999), oi.SubscriptionStart) AS expiration_date,
		revoked_since,
		lic_origin
	FROM
		licenses AS l 
		LEFT JOIN CRM.dbo.OrderItems AS oi ON oi.Id = l.order_item_id
),

enterprise_clients AS (
	SELECT
		Customer_Id AS customer_id
	FROM 
		DXStatisticsV2.dbo.UserInGroups
	WHERE 
		UserGroup_Id = '943B96B1-7C80-11E5-BF27-6470020143F0' --Barclays licensed customers
),

user_posts_within_period AS (
	SELECT
		posts.Created AS post_creation_timestamp,
		posts.Ticket_Id AS ticked_id,
		users.FriendlyId AS user_id,
		users.PublicName AS user_name,
		IIF(EXISTS( 
				SELECT end_user_id 
				FROM licenses_with_periods 
				WHERE end_user_id = users.CRMid AND posts.Created BETWEEN subscription_start AND expiration_date
			) OR
			users.CRMid IN (	
				SELECT customer_id 
				FROM enterprise_clients
			), 
			@licensed,
				IIF(posts.Created < (	
						SELECT ISNULL(MIN(subscription_start), DATEFROMPARTS(9999,01,01)) 
						FROM licenses_with_periods 
						WHERE end_user_id = users.CRMid
					), 
					@trial, 
						IIF(posts.Created > (	
								SELECT IIF(MAX(lic_origin) = @historical_lic_origin, MAX(revoked_since), DATEFROMPARTS(9999,01,01)) 
								FROM licenses_with_periods 
								WHERE end_user_id = users.CRMid
							), 
							@revoked, 
								@expired))) AS license_status
	FROM 
		DXStatisticsV2.dbo.Posts AS posts
		INNER JOIN DXStatisticsV2.dbo.Users AS users ON users.Id = posts.Owner
		LEFT JOIN crm.dbo.Employees AS e ON e.Id = users.CRMid
	WHERE
		e.Id IS NULL AND
		users.FriendlyId NOT IN ('A2151720') AND
		posts.Created BETWEEN @period_start AND @period_end
),

user_posts_within_period_with_tribes AS (
	SELECT
		posts.post_creation_timestamp,
		posts.user_id,
		posts.user_name,
		tribes.Name AS tribe_name,
		tribes.Id AS tribe_id,
		license_status,
		posts.ticked_id
	FROM user_posts_within_period AS posts
		LEFT JOIN DXStatisticsV2.dbo.TicketInfos AS ti ON ti.Id = posts.ticked_id
		LEFT JOIN DXStatisticsV2.dbo.TribeTeamMapping AS ttm ON ttm.SupportTeam = ISNULL(ti.ProcessingSupportTeam, ti.SupportTeam)
		INNER JOIN crm.dbo.Tribes AS tribes ON ttm.Tribe = tribes.Id
),

user_posts_by_tribes AS (
	SELECT 
		user_id,
		MIN(user_name) AS user_name,
		CASE license_status
			WHEN @licensed THEN 'Licensed'
			WHEN @expired THEN 'Expired'
			WHEN @revoked THEN 'Revoked'
			ELSE 'Trial'
		END AS license_status,
		MIN(tribe_name) AS tribe_name,
		COUNT(post_creation_timestamp) AS user_posts_by_tribe,
		SUM(COUNT(post_creation_timestamp)) OVER(PARTITION BY user_id) AS user_posts,
		COUNT(DISTINCT ticked_id) AS user_tickets_by_tribe,
		SUM(COUNT(post_creation_timestamp)) OVER() AS posts_from_all_users
	FROM 
		user_posts_within_period_with_tribes
	GROUP BY
		user_id,
		tribe_id,
		license_status
)

SELECT
	user_id 				AS {user_id},
	user_name 				AS {user_name},
	license_status 			AS {license_status},
	tribe_name 				AS {tribe_name},
	user_posts_by_tribe 	AS {user_posts_by_tribe},
	CONVERT(DECIMAL(4,1), user_posts_by_tribe * 100.0 / user_posts) 				AS {user_posts_by_tribe_from_their_all_posts_perc},
	CONVERT(DECIMAL(6,3), user_posts_by_tribe * 100.0 / posts_from_all_users, 2) 	AS {user_posts_by_tribe_from_posts_from_all_users_perc},
	user_posts 				AS {user_posts},
	CONVERT(DECIMAL(6,3), user_posts * 100.0 / posts_from_all_users) 				AS {user_posts_from_posts_from_all_users_perc},
	posts_from_all_users 	AS {posts_from_all_users},
	user_tickets_by_tribe 	AS {user_tickets_by_tribe}
FROM
	user_posts_by_tribes
ORDER BY
	user_posts_from_posts_from_all_users_perc DESC