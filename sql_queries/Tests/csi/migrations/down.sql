SET NOCOUNT ON
SET ANSI_WARNINGS OFF
:setvar SQLCMDERRORLEVEL 1
GO

USE tempdb
DROP DATABASE IF EXISTS SupportCenterPaid
DROP DATABASE IF EXISTS DXStatisticsV2
GO

PRINT 'test db: down'