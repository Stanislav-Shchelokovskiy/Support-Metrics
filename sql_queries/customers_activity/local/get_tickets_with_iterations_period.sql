SELECT 
    MIN(creation_date) AS {period_start}, 
    MAX(creation_date) AS {period_end} 
FROM 
    {table_name}