DROP TABLE IF EXISTS #SaleItemPlatforms;
WITH platform_product_count AS (
SELECT	platform_id								AS platform_id,
		CEILING(COUNT(product_id) * 2.0 / 3)	AS product_cnt_boundary
FROM (	SELECT	platforms.Id			AS platform_id,
				products.Id				AS product_id,
				platform_tribe.Id		AS platform_tribe_id,
				product_tribe.Id		AS product_tribe_id,
				platform_tribe.Name		AS platform_tribe_name,
				platforms.Name			AS platform_name,
				product_tribe.Name		AS product_tribe_name,
				products.Name			AS product_name
		FROM (	SELECT DISTINCT Product_Id, Platform_Id 
				FROM CRM.dbo.SaleItemBuild_Product_Plaform
			 )	AS sibpp
			  INNER JOIN CRM.dbo.Platforms	AS platforms		ON platforms.Id = sibpp.Platform_Id
			  INNER JOIN CRM.dbo.Products	AS products			ON products.Id = sibpp.Product_Id
			  INNER JOIN CRM.dbo.Tribes		AS platform_tribe	ON platform_tribe.Id = platforms.DefaultTribe
			  LEFT JOIN CRM.dbo.Tribes		AS product_tribe	ON product_tribe.Id = products.Tribe_Id
		WHERE platforms.DefaultTribe IS NOT NULL OR products.Tribe_Id IS NOT NULL
	) AS PlatformsProductsTribes
WHERE product_tribe_id = platform_tribe_id
GROUP BY platform_id, platform_name )

SELECT	sib.SaleItem_Id		AS sale_item_id,
		sibpp.platform_id	AS platform_id
INTO	#SaleItemPlatforms
FROM	CRM.dbo.SaleItem_Build AS sib
		CROSS APPLY (
			SELECT	Platform_Id			AS platform_id,
					COUNT(Product_Id)	AS product_cnt
			FROM	CRM.dbo.SaleItemBuild_Product_Plaform
			WHERE	SaleItemBuild_Id = sib.Id
			GROUP BY Platform_Id
		) AS sibpp
		INNER JOIN platform_product_count AS ppc ON ppc.platform_id = sibpp.platform_id 
												AND	ppc.product_cnt_boundary < sibpp.product_cnt
GROUP BY sib.SaleItem_Id, sibpp.platform_id
CREATE CLUSTERED INDEX sib_product_cnt ON #SaleItemPlatforms (sale_item_id, platform_id)
