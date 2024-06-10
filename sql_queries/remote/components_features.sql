SELECT	c.ProcessingTentId  AS {tent_id},
		c.Id     			AS {component_id},
		f.Id     			AS {feature_id},
		c.Name      		AS {component_name},
		f.Name      		AS {feature_name}
FROM 	DXStatisticsV2.dbo.Tent_CaTControlFeatures AS cf
		INNER JOIN DXStatisticsV2.dbo.Tent_CaTControls AS c ON c.Id = cf.ControlId
		INNER JOIN DXStatisticsV2.dbo.Tent_CaTFeatures AS f ON f.Id = cf.FeatureId
UNION
SELECT DISTINCT
		ProcessingTentId						AS tent_id,
		Id										AS component_id,
		'00000000-0000-0000-0000-000000000003'	AS feature_id,
		Name									AS component_name,
		'General'								AS feature_name
FROM	DXStatisticsV2.dbo.Tent_CaTControls
