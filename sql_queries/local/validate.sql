WITH values_to_validate(value) AS (
    SELECT *
    FROM ( VALUES 
        {values}
    )
)

SELECT
    value,
    IIF(EXISTS (SELECT {field} 
                FROM   {table}
                WHERE  {field} = value), 1, 0) AS valid
FROM values_to_validate AS v