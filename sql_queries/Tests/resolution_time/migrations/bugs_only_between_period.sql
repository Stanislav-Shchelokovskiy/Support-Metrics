SET NOCOUNT ON
SET ANSI_WARNINGS OFF
:setvar SQLCMDERRORLEVEL 1
GO

USE SupportCenterPaid
GO

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets
VALUES	(1, 11, DATEADD(YEAR, -40, GETUTCDATE()), 2),
		(2, 22, '2024-04-02 05:49:57', 2)

USE scpaid_audit
GO

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets
VALUES	(1, 0, DATEADD(YEAR, -40, GETUTCDATE()), 'EntityType', 2),
		(2, 0, '2024-04-03 06:49:57', 'EntityType', 2)

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties(Ticket_Id, Name, Value, EntityModified)
VALUES	(1, 'TicketStatus', 'ActiveForDevelopers',	DATEADD(YEAR, -40, GETUTCDATE())),
		(1, 'TicketStatus', 'Closed',				DATEADD(YEAR, -40, DATEADD(HOUR, 2, GETUTCDATE()))),
		(2, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-03 06:53:44'),
		(2, 'TicketStatus', 'Closed',				'2024-04-03 12:22:07')

PRINT 'test db: up'
