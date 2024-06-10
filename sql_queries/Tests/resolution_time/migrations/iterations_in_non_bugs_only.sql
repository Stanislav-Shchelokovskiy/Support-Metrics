SET NOCOUNT ON
SET ANSI_WARNINGS OFF
:setvar SQLCMDERRORLEVEL 1
GO

USE DXStatisticsV2;
GO

DECLARE @question	TINYINT = 1
DECLARE @bug		TINYINT = 2
DECLARE @suggestion	TINYINT = 3
DECLARE @lsc		TINYINT = 7
INSERT INTO Iterations
VALUES	(1, '2024-04-01 05:49:57.957', '2024-04-01 06:48:44.340', @question),
		(2, '2024-04-03 05:49:57.957', '2024-04-03 07:19:44.340', @suggestion),
		(3, '2024-04-04 06:22:07.930', '2024-04-04 09:19:44.340', @bug),
		(4, '2024-04-05 07:22:07.930', '2024-04-05 10:32:07.930', @lsc)

PRINT 'test db: up'
