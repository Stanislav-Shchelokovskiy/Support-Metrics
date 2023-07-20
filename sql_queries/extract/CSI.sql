WITH feedback AS (
	SELECT	t.FriendlyId			AS ticket_scid,
			RatingValue				AS rating_value,
			DateTime				AS date_time,
			CAST(DateTime AS DATE)	AS date,
			DATEDIFF(SECOND, LAG(DateTime, 1, DATEADD(SECOND, 1, DateTime)) OVER (PARTITION BY TicketId ORDER BY DateTime), DateTime) AS delta_secs
	FROM	DXStatisticsV2.dbo.FeedbackItems AS fi
			INNER JOIN SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].Tickets AS t ON t.Id = fi.TicketId
),

feedback_grouped AS (
	SELECT	*,
			/*	Split ratings into half-hour clasters	*/
			SUM(IIF(delta_secs != -1 AND delta_secs <= 1800, 0, 1)) OVER (PARTITION BY ticket_scid ORDER BY date_time) AS rating_group
	FROM	feedback
),

rating_ordered_within_groups AS (
	SELECT	DISTINCT 
			ticket_scid,
			rating_value,
			rating_group,
			date,
			date_time,
			/*	Calculate how often each rating appear within group.	*/
			COUNT(*) OVER (PARTITION BY ticket_scid, rating_group, date, rating_value) AS rating_frequency
	FROM	feedback_grouped
),

most_popular_rating_withing_groups AS (
	SELECT	DISTINCT
			ticket_scid,
			rating_group,
			date,
			/*	If there are multiple different ratings with the same frequency withing group, we take latest from them.	*/
			FIRST_VALUE(rating_value) OVER (PARTITION BY ticket_scid, rating_group, date ORDER BY rating_frequency DESC, date_time DESC) AS rating
	FROM rating_ordered_within_groups
),


feedback_aggregated AS (
	SELECT	ticket_scid,
			date,
			/*	Calculate avg rating over rating groups	*/
			AVG(CAST(rating AS FLOAT)) AS rating
	FROM	most_popular_rating_withing_groups
	GROUP BY ticket_scid, date
)

SELECT	{ticket_scid},
		{date},
		CASE
			WHEN rating <= -0.3 THEN -1
			WHEN rating >= 0.3 THEN 1
			ELSE 0
		END AS {rating}
FROM	feedback_aggregated