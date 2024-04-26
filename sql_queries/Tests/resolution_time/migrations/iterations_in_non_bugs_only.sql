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

DROP TABLE IF EXISTS [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties;
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties (
	Ticket_Id		INT,
	Name			VARCHAR(20),
	Value			VARCHAR(20),
	EntityModified	DATETIME
)

USE DXStatisticsV2;
GO

DECLARE @question	TINYINT = 1
DECLARE @bug		TINYINT = 2
DECLARE @suggestion	TINYINT = 3
DECLARE @lsc		TINYINT = 7

DROP TABLE IF EXISTS Iterations;
CREATE TABLE Iterations(
	ticket_scid		INT,
	iteration_start	DATETIME,
	iteration_end	DATETIME,
	ticket_type		INT
)
INSERT INTO Iterations
VALUES	(1, '2024-04-01 05:49:57.957', '2024-04-01 06:48:44.340', @question),
		(2, '2024-04-03 05:49:57.957', '2024-04-03 07:19:44.340', @suggestion),
		(3, '2024-04-04 06:22:07.930', '2024-04-04 09:19:44.340', @bug),
		(4, '2024-04-05 07:22:07.930', '2024-04-05 10:32:07.930', @lsc)
GO

CREATE OR ALTER FUNCTION dbo.get_iterations(@start DATE, @end DATE, @employees VARCHAR(MAX)) RETURNS TABLE AS
RETURN (
		SELECT  *
		FROM Iterations
    )
GO

PRINT 'test db: up'
