SELECT
	t.Id			AS {tribe_id},
	platforms.Id	AS {platform_id},
	Product_Id		AS {product_id},
	platforms.Name	AS {platform_name},
	products.Name	AS {product_name}
FROM 
	CRM.dbo.Platforms AS platforms
	LEFT JOIN CRM.dbo.Platform_Product AS pp ON pp.Platform_Id = platforms.Id
	LEFT JOIN CRM.dbo.Products AS products ON products.Id = pp.Product_Id
	INNER JOIN CRM.dbo.Tribes AS t on t.Id = platforms.DefaultTribe
WHERE
	products.Name IS NOT NULL OR
	(products.Name IS NULL AND pp.Product_Id IS NULL)