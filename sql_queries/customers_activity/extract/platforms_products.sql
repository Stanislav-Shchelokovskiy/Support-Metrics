SELECT
	tr_pl.Id	AS {tribe_id},
	pl.Id		AS {platform_id},
	pr.Id		AS {product_id},
	pl.Name		AS {platform_name},
	pr.Name		AS {product_name}
FROM ( SELECT DISTINCT Product_Id, Platform_Id 
	   FROM CRM.dbo.SaleItemBuild_Product_Plaform) AS sibpp
	INNER JOIN CRM.dbo.Platforms AS pl ON pl.Id = sibpp.Platform_Id
	INNER JOIN CRM.dbo.Products AS pr ON pr.Id = sibpp.Product_Id
	INNER JOIN CRM.dbo.Tribes AS tr_pl ON tr_pl.Id = pl.DefaultTribe