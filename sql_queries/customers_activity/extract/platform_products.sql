SELECT
	t.Id			AS {tribe_id},
	Platform_Id		AS {platform_id},
	Product_Id		AS {product_id},
	platforms.Name	AS {platform_name},
	products.Name	AS {product_name}
FROM 
	CRM.dbo.Platform_Product AS pp
	INNER JOIN CRM.dbo.Platforms AS platforms ON platforms.Id = pp.Platform_Id
	INNER JOIN CRM.dbo.Products AS products ON products.Id = pp.Product_Id
	INNER JOIN CRM.dbo.Tribes AS t on t.Id = platforms.DefaultTribe