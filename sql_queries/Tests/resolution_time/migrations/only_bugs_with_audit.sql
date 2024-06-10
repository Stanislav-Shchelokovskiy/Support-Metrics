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
VALUES	(1, 0, '2024-04-03 06:54:04', 'EntityType', 1),
		(2, 0, '2024-04-03 06:49:57', 'EntityType', 2)

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties(Ticket_Id, Name, Value, EntityModified)
VALUES	(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-01 05:19:01'),
		(1, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-01 09:21:02'),
		(1, 'TicketStatus', 'Closed',				'2024-04-02 06:23:03'),
		(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-03 05:54:04'),
		(1, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-03 07:55:05'),
		(1, 'TicketStatus', 'Closed',				'2024-04-03 08:56:06'),
		(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-05 05:54:04'),
		(1, 'TicketStatus', 'Closed',				'2024-04-05 06:26:06'),

		(2, 'TicketStatus', 'ActiveForSupport',		'2024-04-02 05:49:57'),
		(2, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-02 09:21:02'),
		(2, 'TicketStatus', 'Closed',				'2024-04-02 13:23:03'),
		(2, 'TicketStatus', 'ActiveForSupport',		'2024-04-03 05:49:57'),
		(2, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-03 06:53:44'),
		(2, 'TicketStatus', 'Closed',				'2024-04-03 09:22:07')

PRINT 'test db: up'
