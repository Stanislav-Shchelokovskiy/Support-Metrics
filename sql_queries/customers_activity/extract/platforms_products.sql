SELECT
	platform_tribe.id								AS {platform_tribe_id},
	platforms.Id									AS {platform_id},
	ISNULL(product_tribe.Id, platform_tribe.id)		AS {product_tribe_id},
	products.Id										AS {product_id},
	platform_tribe.Name								AS {platform_tribe_name},
	platforms.Name									AS {platform_name},
	ISNULL(product_tribe.Name, platform_tribe.Name)	AS {product_tribe_name},
	products.Name									AS {product_name}
FROM (SELECT DISTINCT Product_Id, Platform_Id 
	  FROM CRM.dbo.SaleItemBuild_Product_Plaform
	  WHERE AuxiliaryPackage = 0) AS sibpp
	  INNER JOIN CRM.dbo.Platforms AS platforms ON platforms.Id = sibpp.Platform_Id
	  INNER JOIN CRM.dbo.Products AS products ON products.Id = sibpp.Product_Id
	  INNER JOIN CRM.dbo.Tribes AS platform_tribe ON platform_tribe.Id = platforms.DefaultTribe
	  LEFT JOIN CRM.dbo.Tribes AS product_tribe ON product_tribe.Id = products.Tribe_Id
WHERE platforms.DefaultTribe IS NOT NULL OR products.Tribe_Id IS NOT NULL