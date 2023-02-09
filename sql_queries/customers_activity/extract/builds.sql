SELECT 
    id AS {id}, 
    id AS {name}
FROM (
	SELECT DISTINCT CONCAT(FORMAT(Number, '0.#'),'.', BuildNumber) AS id
	FROM CRM.dbo.Builds AS b
	LEFT JOIN CRM.dbo.Versions AS v ON v.Id = b.Version_Id
	WHERE Number BETWEEN DATEPART(YEAR,	GETUTCDATE()) % 2000 - 4 AND 100
) AS b