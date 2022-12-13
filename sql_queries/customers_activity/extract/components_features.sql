SELECT
    ttm.Tribe   AS {tribe_id},
	Control     AS {component_id},
    Feature     AS {feature_id},
	c.Name      AS {component_name},
	f.Name      AS {feature_name}
FROM DXStatisticsV2.dbo.CaTControlFeatures AS cf
INNER JOIN DXStatisticsV2.dbo.CaTControls AS c ON c.Id = cf.Control
INNER JOIN DXStatisticsV2.dbo.CaTFeatures AS f ON f.Id = cf.Feature
INNER JOIN DXStatisticsV2.dbo.TribeTeamMapping AS ttm ON ttm.SupportTeam = c.SupportTeamId
INNER JOIN CRM.dbo.Tribes AS tribes ON ttm.Tribe = tribes.Id