DECLARE @start_date DATE = '{start_date}'

SELECT  {tribe_id},
        {tent_id},
        {position_id},
        {crmid},
        {scid},
        {name},
        {tribe_name},
        {tent_name},
        {position_name}
FROM    DXStatisticsV2.dbo.support_analytics_employees()
WHERE   retired_at IS NULL OR retired_at > @start_date