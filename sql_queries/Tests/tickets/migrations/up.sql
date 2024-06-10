SET NOCOUNT ON
SET ANSI_WARNINGS OFF
:setvar SQLCMDERRORLEVEL 1
GO

CREATE DATABASE CRMAudit
CREATE DATABASE DXStatisticsV2
CREATE DATABASE CRM
CREATE DATABASE SupportCenterPaid
CREATE DATABASE scpaid_audit
GO


USE CRM
GO

CREATE TABLE SaleItems (
	Id			UNIQUEIDENTIFIER,
	Parent		UNIQUEIDENTIFIER,
	Name		VARCHAR(30),
	IsTraining	BIT
)

CREATE TABLE SaleItem_Build (
	Id			UNIQUEIDENTIFIER,
	SaleItem_Id	UNIQUEIDENTIFIER
)

CREATE TABLE SaleItemBuild_Product_Plaform(
	SaleItemBuild_Id	UNIQUEIDENTIFIER,
	Product_Id			UNIQUEIDENTIFIER,
	Platform_Id			UNIQUEIDENTIFIER
)

CREATE TABLE Platforms (
	Id				UNIQUEIDENTIFIER,
	Name			VARCHAR(20),
	DefaultTribe	UNIQUEIDENTIFIER
)

CREATE TABLE Products (
	Id				UNIQUEIDENTIFIER,
	Name			VARCHAR(20),
	Tribe_Id	UNIQUEIDENTIFIER
)

CREATE TABLE Tribes (
	Id		UNIQUEIDENTIFIER,
	Name	VARCHAR(20),
)
INSERT INTO Tribes
VALUES	('00000000-0000-0000-0000-000000000001', 'tribe1'),
		('00000000-0000-0000-0000-000000000002', 'tribe2'),
		('00000000-0000-0000-0000-000000000003', 'tribe3')

CREATE TABLE Licenses (
	Id				UNIQUEIDENTIFIER,
	Owner_Id		UNIQUEIDENTIFIER,
	EndUser_Id		UNIQUEIDENTIFIER,
	OrderItem_Id	UNIQUEIDENTIFIER
)

CREATE TABLE OrderItems (
	Id					UNIQUEIDENTIFIER,
	SaleItem_Id			UNIQUEIDENTIFIER,
	Order_Id			UNIQUEIDENTIFIER,
	SubscriptionStart	DATETIME,
	HoldingPeriod		INT
)

CREATE TABLE Orders (
	Id		UNIQUEIDENTIFIER,
	Status	INT
)

CREATE TABLE License_FreeSaleItem(
	FreeSaleItem_Id	UNIQUEIDENTIFIER,
	License_Id		UNIQUEIDENTIFIER
)

CREATE TABLE Customers(
	Id				UNIQUEIDENTIFIER,
	FriendlyId		VARCHAR(20),
	RegisterDate	DATE
)

CREATE TABLE Customer_UserGroup(
	UserGroup_Id	UNIQUEIDENTIFIER,
	Customer_Id		UNIQUEIDENTIFIER
)

USE CRMAudit
GO

CREATE SCHEMA dxcrm
GO

CREATE TABLE dxcrm.Licenses (
	EntityOid			UNIQUEIDENTIFIER,
	Owner_Id			UNIQUEIDENTIFIER,
	EndUser_Id			UNIQUEIDENTIFIER,
	OrderItem_Id		UNIQUEIDENTIFIER,
	ChangedProperties	VARCHAR(20),
	EntityModified		DATETIME
)

USE SupportCenterPaid
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].UserInGroup (
	User_Id			UNIQUEIDENTIFIER,
	UserGroup_Id	UNIQUEIDENTIFIER
)

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets (
	Id			UNIQUEIDENTIFIER,
	FriendlyId	VARCHAR(35),
	EntityType	INT,
	Created		DATETIME,
	Owner		UNIQUEIDENTIFIER,
	IsPrivate	BIT
)

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties (
	Ticket_Id	UNIQUEIDENTIFIER,
	Name		VARCHAR(20),
	Value		VARCHAR(40)
)

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].Users (
	Id			UNIQUEIDENTIFIER,
	FriendlyId	VARCHAR(20),
	IsEmployee	BIT
)

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags (
	Tickets	UNIQUEIDENTIFIER,
	Tags	UNIQUEIDENTIFIER
)

USE scpaid_audit
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO

CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties (
	AuditOwner			UNIQUEIDENTIFIER,
	Ticket_Id			UNIQUEIDENTIFIER,
	EntityModified		DATETIME,
	Name				VARCHAR(20),
	Value				VARCHAR(20),	
)

CREATE TABLE  [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets (
	EntityOid			UNIQUEIDENTIFIER,
	AuditAction			INT,
	Modified			DATETIME,
	ChangedProperties	VARCHAR(20) DEFAULT 'EntityType',
	EntityType			INT
)

USE DXStatisticsV2
GO

CREATE FUNCTION dbo.get_ticket_tribes(@ticket_id UNIQUEIDENTIFIER, @ticket_type TINYINT = NULL, @priority_tribe_id UNIQUEIDENTIFIER = NULL)
RETURNS @tribes TABLE
(
    id UNIQUEIDENTIFIER NOT NULL,
    name NVARCHAR(100)
)
AS
BEGIN
DECLARE @most_suitable  TINYINT = 3
DECLARE @suitable       TINYINT = 2
DECLARE @less_suitable  TINYINT = 1
DECLARE @least_suitable TINYINT = 0

DECLARE @lsc            TINYINT = 7
DECLARE @dev_tribe_id   UNIQUEIDENTIFIER = '340E06F5-9B98-4923-97A4-CA02BA73F075'

INSERT INTO @tribes
SELECT Id, Name
FROM CRM.dbo.Tribes
WHERE Id IN (
        SELECT Id
        FROM (  SELECT *, MAX(suitability) OVER() AS max_suitability
                FROM (  SELECT TOP 1 tp.Value AS Id, @most_suitable AS suitability
                        FROM    SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties AS tp
                                        INNER JOIN CRM.dbo.Tribes AS tribes ON tribes.Id = tp.Value
                        WHERE   tp.Ticket_Id = @ticket_id
                                AND     tp.Name IN ('ProcessingTribe', 'Tribe')
                        ORDER BY tp.Name
                        UNION
                        SELECT  Tribe_Id, @suitable
                        FROM    CRM.dbo.Products
                        WHERE   Id IN ( SELECT  Value
                                        FROM    SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
                                        WHERE   Ticket_Id = @ticket_id  AND Name = 'ProductId')
                                            AND Tribe_Id IS NOT NULL
                        UNION
                        SELECT DefaultTribe, @less_suitable
                        FROM   CRM.dbo.Platforms
                        WHERE  Id IN (  SELECT  Value
                                        FROM    SupportCenterPaid.[c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
                                        WHERE   Ticket_Id = @ticket_id AND Name = 'PlatformedProductId' AND Value NOT LIKE '%:%')
                        UNION 
                        SELECT @dev_tribe_id, @least_suitable
                    ) AS ti
                ) AS tribes_inner
        WHERE id IS NOT NULL AND suitability = max_suitability)
RETURN 
END
GO

CREATE TABLE TicketsTents(
	Ticket_Id	UNIQUEIDENTIFIER,
	id			UNIQUEIDENTIFIER,
	name		VARCHAR(20)
)
GO

CREATE FUNCTION dbo.get_ticket_tent(@ticket_id UNIQUEIDENTIFIER)RETURNS TABLE AS
RETURN (
    SELECT TOP 1 id, name
    FROM	TicketsTents
    WHERE  Ticket_Id = @ticket_id
)
GO
