SELECT 
    DATE(MIN(creation_date), '+{rank_period_offset}') AS {period_start}, 
    MAX(creation_date) AS {period_end} 
FROM 
    {table_name}