SELECT
	tent_platform.Tent_Id								AS {platform_tent_id},
	platforms.Id										AS {platform_id},
	ISNULL(tent_product.Tent_Id, tent_platform.Tent_Id)	AS {product_tent_id},
	products.Id											AS {product_id},
	platform_tent.Name									AS {platform_tent_name},
	platforms.Name										AS {platform_name},
	ISNULL(product_tent.Name, platform_tent.Name)		AS {product_tent_name},
	products.Name										AS {product_name}
FROM (SELECT DISTINCT Product_Id, Platform_Id 
	  FROM CRM.dbo.SaleItemBuild_Product_Plaform
	  WHERE AuxiliaryPackage = 0)		AS sibpp
	  INNER JOIN CRM.dbo.Platforms		AS platforms		ON platforms.Id					= sibpp.Platform_Id
	  LEFT JOIN CRM.dbo.Tent_Platform	AS tent_platform	ON tent_platform.Platform_Id	= sibpp.Platform_Id
	  INNER JOIN CRM.dbo.Products		AS products			ON products.Id					= sibpp.Product_Id
	  LEFT JOIN CRM.dbo.Tent_Product	AS tent_product		ON tent_product.Product_Id		= sibpp.Product_Id
	  LEFT JOIN CRM.dbo.Tents			AS platform_tent	ON platform_tent.Id				= tent_platform.Tent_Id
	  LEFT JOIN CRM.dbo.Tents			AS product_tent		ON product_tent.Id				= tent_product.Tent_Id
WHERE platforms.DefaultTribe IS NOT NULL OR products.Tribe_Id IS NOT NULL