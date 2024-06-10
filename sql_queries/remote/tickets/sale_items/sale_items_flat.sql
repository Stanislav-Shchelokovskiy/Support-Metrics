DECLARE @separator CHAR = ';'

DROP TABLE IF EXISTS #SaleItemsFlat;
WITH sale_items_flat AS (
	SELECT	Id AS id,
			Parent AS parent,
			Name AS name,
			CONVERT(NVARCHAR(MAX), id) AS items,
			0 AS level
	FROM	CRM.dbo.SaleItems AS si
	WHERE	IsTraining = 0
	UNION ALL
	SELECT	si.Id,
			si.Parent,
			si.Name,
			sif.items + IIF(LEN(sif.items)>0, @separator, '') + CONVERT(NVARCHAR(MAX), si.id) AS items,
			sif.level + 1
	FROM	sale_items_flat	AS sif
			INNER JOIN CRM.dbo.SaleItems AS si ON si.Id = sif.parent
)

SELECT	id			AS id,
		name		AS name,
		items.item	AS item
INTO	#SaleItemsFlat
FROM	sale_items_flat
		CROSS APPLY (
			SELECT DISTINCT CAST(value AS UNIQUEIDENTIFIER) AS item
			FROM STRING_SPLIT(items, @separator)
		) AS items
GROUP BY id, name, items.item
CREATE CLUSTERED INDEX idx_id ON #SaleItemsFlat (id)
