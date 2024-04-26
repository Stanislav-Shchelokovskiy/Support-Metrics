SET NOCOUNT ON
SET ANSI_WARNINGS OFF
:setvar SQLCMDERRORLEVEL 1
GO

CREATE DATABASE DXStatisticsV2
CREATE DATABASE scpaid_audit
CREATE DATABASE SupportCenterPaid
GO

USE SupportCenterPaid
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO

DROP TABLE IF EXISTS [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets;
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets (
	Id			INT,
	FriendlyId	INT,
	Created		DATETIME,
	EntityType	INT

);
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets
VALUES	(1, 11, '2024-04-01 05:19:01', 2),
		(2, 22, '2024-04-02 05:49:57', 2)


USE scpaid_audit
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO

DROP TABLE IF EXISTS [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets;
CREATE TABLE  [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets (
	EntityOid			INT,
	AuditAction			INT,
	Modified			DATETIME,
	ChangedProperties	VARCHAR(20) DEFAULT 'EntityType',
	EntityType			INT
)

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets
VALUES	(1, 1, '2024-04-03 07:54:04', 'EntityType', 2),
		(2, 0, '2024-04-03 06:49:57', 'EntityType', 2)

DROP TABLE IF EXISTS [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties;
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties (
	Ticket_Id		INT,
	Name			VARCHAR(20),
	Value			VARCHAR(20),
	EntityModified	DATETIME
)


INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties(Ticket_Id, Name, Value, EntityModified)
VALUES	(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-01 05:19:01'),
		(1, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-01 09:21:02'),
		(1, 'TicketStatus', 'Closed',				'2024-04-02 06:23:03'),
		(1, 'TicketStatus', 'ActiveForSupport',		'2024-04-03 05:54:04'),
		(1, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-03 07:55:05'),
		
		(2, 'TicketStatus', 'ActiveForDevelopers',	'2024-04-03 06:53:44'),
		(2, 'TicketStatus', 'Closed',				'2024-04-03 09:22:07')
GO

USE DXStatisticsV2;
GO

DROP TABLE IF EXISTS Iterations
CREATE TABLE Iterations(
	ticket_scid		INT,
	iteration_start	DATETIME,
	iteration_end	DATETIME,
	ticket_type		INT
)
GO

CREATE OR ALTER FUNCTION dbo.get_iterations(@start DATE, @end DATE, @employees VARCHAR(MAX)) RETURNS TABLE AS
RETURN (
		SELECT  *
		FROM Iterations
    )
GO

PRINT 'test db: up'
