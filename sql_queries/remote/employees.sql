DECLARE @employees VARCHAR(MAX) = N'{employees_json}'
DECLARE @start DATE = '{start_date}'

SELECT  {tribe_id},
        {tent_id},
        {position_id},
        {crmid},
        {scid},
        {name},
        {tribe_name},
        {tent_name},
        {position_name},
        {roles}
FROM    DXStatisticsV2.dbo.parse_employees(@employees)
WHERE   (retired_at IS NULL OR retired_at > @start)
    AND is_service_user = 0
