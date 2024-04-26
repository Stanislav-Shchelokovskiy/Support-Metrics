DROP TABLE IF EXISTS #SaleItemProducts
SELECT	sib.SaleItem_Id		AS sale_item_id,
		sibpp.Product_Id	AS product_id
INTO	#SaleItemProducts
FROM	CRM.dbo.SaleItem_Build AS sib
		INNER JOIN CRM.dbo.SaleItemBuild_Product_Plaform AS sibpp ON sibpp.SaleItemBuild_Id = sib.Id
GROUP BY sib.SaleItem_Id, sibpp.Product_Id
CREATE CLUSTERED INDEX si_products ON #SaleItemProducts (sale_item_id, product_id)
