DECLARE @employees VARCHAR(MAX) = N'{employees_json}'

SELECT DISTINCT roles.value                 AS {id},
                TRIM('()' FROM roles.value) AS {name} 
FROM    DXStatisticsV2.dbo.parse_employees(@employees) AS e
        OUTER APPLY (
            SELECT value
            FROM STRING_SPLIT(e.roles, ';')
        ) AS roles
WHERE roles.value IS NOT NULL
