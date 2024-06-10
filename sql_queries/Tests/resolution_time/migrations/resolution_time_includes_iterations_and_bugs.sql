SET NOCOUNT ON
SET ANSI_WARNINGS OFF
:setvar SQLCMDERRORLEVEL 1
GO

USE SupportCenterPaid
GO

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets
VALUES	(1, 11, '2024-04-01 05:19:01', 2),
		(2, 22, '2024-04-02 05:49:57', 2)


USE scpaid_audit
GO

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets
VALUES	(1, 0, '2024-04-03 05:54:04', 'EntityType', 2),
		(2, 0, '2024-04-02 06:49:57', 'EntityType', 2)

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties(Ticket_Id, Name, Value, EntityModified)
VALUES	(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-01 05:19:01'),
		(1, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-01 09:21:02'),
		(1, 'TicketStatus', 'Closed',				'2024-04-02 06:23:03'),
		(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-03 05:54:04'),
		(1, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-03 07:55:05'),
		(1, 'TicketStatus', 'Closed',				'2024-04-04 06:26:06'),
		(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-05 05:54:04'),
		(1, 'TicketStatus', 'Closed',				'2024-04-05 06:26:06'),

		(2, 'ShouldIgnnore', 'ActiveForDevelopers',	'2024-04-03 07:53:44'),
		(2, 'ShouldIgnnore', 'Closed',				'2024-04-04 03:22:07')

USE DXStatisticsV2;
GO

INSERT INTO Iterations
VALUES	
		(3, '2024-04-01 05:49:57.957', '2024-04-01 06:49:44.340', 1),
		(3, '2024-04-03 05:49:57.957', '2024-04-03 06:19:44.340', 1),
		(3, '2024-04-04 06:22:07.930', '2024-04-04 08:19:44.340', 1),
		(3, '2024-04-05 07:22:07.930', '2024-04-05 08:32:07.930', 1)

PRINT 'test db: up'
