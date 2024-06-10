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

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets (
	Id			INT,
	FriendlyId	INT,
	Created		DATETIME,
	EntityType	INT

)

USE scpaid_audit
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO

CREATE TABLE  [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets (
	EntityOid			INT,
	AuditAction			INT,
	Modified			DATETIME,
	ChangedProperties	VARCHAR(20) DEFAULT 'EntityType',
	EntityType			INT
)

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties (
	Ticket_Id		INT,
	Name			VARCHAR(20),
	Value			VARCHAR(20),
	EntityModified	DATETIME
)

USE DXStatisticsV2;
GO

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
