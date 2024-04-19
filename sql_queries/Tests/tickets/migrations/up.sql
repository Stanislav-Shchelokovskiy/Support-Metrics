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

--SaleItems--
CREATE TABLE SaleItems (
	Id			UNIQUEIDENTIFIER,
	Parent		UNIQUEIDENTIFIER,
	Name		VARCHAR(30),
	IsTraining	BIT
)
INSERT INTO SaleItems
VALUES	('00000000-0000-0000-0000-000000000001',	NULL,									'universal',	0),
		('00000000-0000-0000-0000-000000000002',	'00000000-0000-0000-0000-000000000001',	'dxp',			0),
		('00000000-0000-0000-0000-000000000003',	'00000000-0000-0000-0000-000000000002',	'devextreme',	0),
		('00000000-0000-0000-0000-000000000004',	NULL,									'free bundle',	0),
		('00000000-0000-0000-0000-000000000005',	NULL,									'training',		1)
		
--SaleItem_Build--
CREATE TABLE SaleItem_Build (
	Id			UNIQUEIDENTIFIER,
	SaleItem_Id	UNIQUEIDENTIFIER
)
INSERT INTO SaleItem_Build
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000003'),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000004')

--SaleItemBuild_Product_Plaform--
CREATE TABLE SaleItemBuild_Product_Plaform(
	SaleItemBuild_Id	UNIQUEIDENTIFIER,
	Product_Id			UNIQUEIDENTIFIER,
	Platform_Id			UNIQUEIDENTIFIER
)
INSERT INTO SaleItemBuild_Product_Plaform
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000001'),

		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000006', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000007', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000008', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000009', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000010', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000011', '00000000-0000-0000-0000-000000000003'),

		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000012', '00000000-0000-0000-0000-000000000004'),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000013', '00000000-0000-0000-0000-000000000004'),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000014', '00000000-0000-0000-0000-000000000004'),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000015', '00000000-0000-0000-0000-000000000004')

--Platforms--
CREATE TABLE Platforms (
	Id				UNIQUEIDENTIFIER,
	Name			VARCHAR(20),
	DefaultTribe	UNIQUEIDENTIFIER
)
INSERT INTO Platforms
VALUES	('00000000-0000-0000-0000-000000000001', 'platform1',			'00000000-0000-0000-0000-000000000001'	),
		('00000000-0000-0000-0000-000000000002', 'platform2',			'00000000-0000-0000-0000-000000000002'	),
		('00000000-0000-0000-0000-000000000003', 'should be ignored',	NULL									),
		('00000000-0000-0000-0000-000000000004', 'platform4',			'00000000-0000-0000-0000-000000000003'	)

--Products--
CREATE TABLE Products (
	Id				UNIQUEIDENTIFIER,
	Name			VARCHAR(20),
	Tribe_Id	UNIQUEIDENTIFIER
)
INSERT INTO Products
VALUES	('00000000-0000-0000-0000-000000000001', 'product1',			'00000000-0000-0000-0000-000000000001'	),
		('00000000-0000-0000-0000-000000000002', 'product2',			'00000000-0000-0000-0000-000000000001'	),
		('00000000-0000-0000-0000-000000000003', 'product3',			'00000000-0000-0000-0000-000000000001'	),
		('00000000-0000-0000-0000-000000000004', 'product4',			'00000000-0000-0000-0000-000000000002'	),
		('00000000-0000-0000-0000-000000000005', 'product5',			'00000000-0000-0000-0000-000000000002'	),
		('00000000-0000-0000-0000-000000000006', 'product6',			'00000000-0000-0000-0000-000000000003'	),
		('00000000-0000-0000-0000-000000000007', 'product7',			'00000000-0000-0000-0000-000000000003'	),
		('00000000-0000-0000-0000-000000000008', 'product8',			'00000000-0000-0000-0000-000000000003'	),
		('00000000-0000-0000-0000-000000000009', 'product9',			'00000000-0000-0000-0000-000000000003'	),
		('00000000-0000-0000-0000-000000000010', 'product10',			'00000000-0000-0000-0000-000000000002'	),
		('00000000-0000-0000-0000-000000000011', 'should be ignored',	NULL									),
		('00000000-0000-0000-0000-000000000012', 'product12',			'00000000-0000-0000-0000-000000000003'	),
		('00000000-0000-0000-0000-000000000013', 'product13',			'00000000-0000-0000-0000-000000000003'	),
		('00000000-0000-0000-0000-000000000014', 'product14',			'00000000-0000-0000-0000-000000000003'	),
		('00000000-0000-0000-0000-000000000015', 'product15',			'00000000-0000-0000-0000-000000000003'	)

--Tribes--
CREATE TABLE Tribes (
	Id		UNIQUEIDENTIFIER,
	Name	VARCHAR(20),
)
INSERT INTO Tribes
VALUES	('00000000-0000-0000-0000-000000000001', 'tribe1'),
		('00000000-0000-0000-0000-000000000002', 'tribe2'),
		('00000000-0000-0000-0000-000000000003', 'tribe3')

--Licenses--
CREATE TABLE Licenses (
	Id				UNIQUEIDENTIFIER,
	Owner_Id		UNIQUEIDENTIFIER,
	EndUser_Id		UNIQUEIDENTIFIER,
	OrderItem_Id	UNIQUEIDENTIFIER
)
INSERT INTO Licenses
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000003'),
		('00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000006', '00000000-0000-0000-0000-000000000004')

--OrderItems--
CREATE TABLE OrderItems (
	Id					UNIQUEIDENTIFIER,
	SaleItem_Id			UNIQUEIDENTIFIER,
	Order_Id			UNIQUEIDENTIFIER,
	SubscriptionStart	DATETIME,
	HoldingPeriod		INT
)
INSERT INTO OrderItems
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001', '2023-06-01 11:54:44', 365),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000002', '2023-01-01 11:54:44', 365),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000003', '2023-02-01 11:54:44', 365),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000004', '2023-01-01 11:54:44', 365)

--Orders--
CREATE TABLE Orders (
	Id		UNIQUEIDENTIFIER,
	Status	INT
)
DECLARE @paid		  TINYINT = 5
DECLARE @free_license TINYINT = 6
INSERT INTO Orders
VALUES	('00000000-0000-0000-0000-000000000001', @paid),
		('00000000-0000-0000-0000-000000000002', @paid),
		('00000000-0000-0000-0000-000000000003', @free_license),
		('00000000-0000-0000-0000-000000000004', @paid)

--License_FreeSaleItem--
CREATE TABLE License_FreeSaleItem(
	FreeSaleItem_Id	UNIQUEIDENTIFIER,
	License_Id		UNIQUEIDENTIFIER
)
INSERT INTO License_FreeSaleItem
VALUES	('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000001')

--Customers--
CREATE TABLE Customers(
	Id				UNIQUEIDENTIFIER,
	FriendlyId		VARCHAR(20),
	RegisterDate	DATE
)
INSERT INTO Customers
VALUES	('00000000-0000-0000-0000-000000000001', 'user1',		'2022-01-01'	),
		('00000000-0000-0000-0000-000000000002', 'user2',		NULL			),
		('00000000-0000-0000-0000-000000000003', 'user3',		'2022-03-01'	),
		('00000000-0000-0000-0000-000000000004', 'user4',		'2022-04-01'	),
		('00000000-0000-0000-0000-000000000005', 'user5',		'2022-04-01'	),
		('00000000-0000-0000-0000-000002151720', 'doc.ctor',	NULL			)

--Customer_UserGroup--
CREATE TABLE Customer_UserGroup(
	UserGroup_Id	UNIQUEIDENTIFIER,
	Customer_Id		UNIQUEIDENTIFIER
)
INSERT INTO Customer_UserGroup
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000003'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000002')


USE CRMAudit
GO

CREATE SCHEMA dxcrm
GO

--Licenses--
DROP TABLE IF EXISTS dxcrm.Licenses;
CREATE TABLE dxcrm.Licenses (
	EntityOid			UNIQUEIDENTIFIER,
	Owner_Id			UNIQUEIDENTIFIER,
	EndUser_Id			UNIQUEIDENTIFIER,
	OrderItem_Id		UNIQUEIDENTIFIER,
	ChangedProperties	VARCHAR(20),
	EntityModified		DATETIME
)
INSERT INTO dxcrm.Licenses
VALUES	('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000004', 'EndUser', '2023-07-01 11:54:44'),
		('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001', 'EndUser', '2024-02-01 11:54:44')


USE SupportCenterPaid
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO

--UserInGroup--
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].UserInGroup (
	User_Id			UNIQUEIDENTIFIER,
	UserGroup_Id	UNIQUEIDENTIFIER
)
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].UserInGroup
VALUES	('00000000-0000-0000-0000-000000000004', '943B96B1-7C80-11E5-BF27-6470020143F0')

--Tickets--
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets (
	Id			UNIQUEIDENTIFIER,
	FriendlyId	VARCHAR(35),
	EntityType	INT,
	Created		DATETIME,
	Owner		UNIQUEIDENTIFIER,
	IsPrivate	BIT
)
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets
VALUES	('00000000-0000-0000-0000-000000000001', 'trial (11)',						1,  '2023-02-01 11:54:44', '00000000-0000-0000-0000-000000000001', 1),
		('00000000-0000-0000-0000-000000000002', 'licensed (0)',					1,  '2023-07-01 11:54:44', '00000000-0000-0000-0000-000000000001', 1),
		('00000000-0000-0000-0000-000000000003', 'assigned_to_someone (4)',			1,  '2023-08-01 11:54:44', '00000000-0000-0000-0000-000000000005', 1),
		('00000000-0000-0000-0000-000000000004', 'licensed (0)',					1,  '2024-01-01 11:54:44', '00000000-0000-0000-0000-000000000002', 1),
		('00000000-0000-0000-0000-000000000005', 'revoked (3)',						1,  '2024-04-02 11:54:44', '00000000-0000-0000-0000-000000000002', 1),
		('00000000-0000-0000-0000-000000000006', 'expired (2)',						1,  '2024-06-02 11:54:44', '00000000-0000-0000-0000-000000000001', 1),
		('00000000-0000-0000-0000-000000000007', 'no license (5)',					2,  '2023-02-02 11:54:44', '00000000-0000-0000-0000-000000000003', 1),
		('00000000-0000-0000-0000-000000000008', 'licensed (0)',					6,  '2023-02-03 11:54:44', '00000000-0000-0000-0000-000000000003', 1),
		('00000000-0000-0000-0000-000000000009', 'no_license_revoked (6)',			1,  '2024-04-02 11:54:44', '00000000-0000-0000-0000-000000000002', 1),
		('00000000-0000-0000-0000-000000000010', 'no_license_expired (7)',			2,  '2024-02-02 11:54:44', '00000000-0000-0000-0000-000000000003', 1),
		('00000000-0000-0000-0000-000000000011', 'no_license_expired_revoked (8)',	1,  '2024-07-02 11:54:44', '00000000-0000-0000-0000-000000000002', 1),
		('00000000-0000-0000-0000-000000000012', 'trial (11)',						1,  '2023-01-02 11:54:44', '00000000-0000-0000-0000-000000000004', 1),
		('00000000-0000-0000-0000-000000000013', 'no_license_free (9)',				1,  '2023-03-02 11:54:44', '00000000-0000-0000-0000-000000000004', 1),
		('00000000-0000-0000-0000-000000000014', 'no_license_expired_free (10)',	1,  '2024-03-02 11:54:44', '00000000-0000-0000-0000-000000000004', 1),
		('00000000-0000-0000-0000-000000000015', 'free (1)',						1,  '2023-03-02 11:54:44', '00000000-0000-0000-0000-000000000004', 1),
		('00000000-0000-0000-0000-000000000016', 'IGNORE',							1,  '2023-03-02 11:54:44', '00000000-0000-0000-0000-000002151720', 1)
		

--TicketProperties--
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties (
	Ticket_Id	UNIQUEIDENTIFIER,
	Name		VARCHAR(20),
	Value		VARCHAR(40)
)
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].TicketProperties
VALUES	('00000000-0000-0000-0000-000000000001', 'PlatformedProductId', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000001', 'ReplyId',				'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000002', 'PlatformedProductId', '00000000-0000-0000-0000-000000000004'),
		('00000000-0000-0000-0000-000000000002', 'ControlId',			'00000000-0000-0000-0000-000000000004'),
		('00000000-0000-0000-0000-000000000003', 'PlatformedProductId', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000003', 'ProductId',			'00000000-0000-0000-0000-000000000006'),
		('00000000-0000-0000-0000-000000000003', 'FeatureId',			'00000000-0000-0000-0000-000000000006'),
		('00000000-0000-0000-0000-000000000004', 'PlatformedProductId', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000004', 'ProductId',			'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000004', 'OperatingSystem',		'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000005', 'PlatformedProductId', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000005', 'ProductId',			'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000005', 'IDE',					'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000006', 'ProductId',			'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000007', 'PlatformedProductId', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000007', 'ProductId',			'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000007', 'Severity',			'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000007', 'FixedInBuild',			'00000000-0000-0000-0000-000000000007'),
		('00000000-0000-0000-0000-000000000008', 'PlatformedProductId', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000008', 'ProductId',			'00000000-0000-0000-0000-000000000011'),
		('00000000-0000-0000-0000-000000000008', 'TicketStatus',		'00000000-0000-0000-0000-000000000011'),
		('00000000-0000-0000-0000-000000000009', 'ProductId',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000009', 'Assignee',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000010', 'ProductId',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000010', 'Duplicate',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000011', 'ProductId',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000011', 'SpecificId',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000013', 'ProductId',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000013', 'BuildId',				'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000014', 'ProductId',			'00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000015', 'ProductId',			'00000000-0000-0000-0000-000000000011')

--Users--
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].Users (
	Id			UNIQUEIDENTIFIER,
	FriendlyId	VARCHAR(20),
	IsEmployee	BIT
)
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].Users
VALUES	('00000000-0000-0000-0000-000000000001', 'user1',		0),
		('00000000-0000-0000-0000-000000000002', 'user2',		0),
		('00000000-0000-0000-0000-000000000003', 'user3',		0),
		('00000000-0000-0000-0000-000000000004', 'user4',		0),
		('00000000-0000-0000-0000-000000000005', 'user5',		0),
		('00000000-0000-0000-0000-000002151720', 'doc.ctor',	1)

--TicketTags--
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags (
	Tickets	UNIQUEIDENTIFIER,
	Tags	UNIQUEIDENTIFIER
)
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].TicketTags 
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000003'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000003'),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000003'),
		('00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000003')


USE scpaid_audit
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO

--scworkflow_TicketProperties--
CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties (
	AuditOwner			UNIQUEIDENTIFIER,
	Ticket_Id			UNIQUEIDENTIFIER,
	EntityModified		DATETIME,
	Name				VARCHAR(20),
	Value				VARCHAR(20),	
)
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_TicketProperties
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2023-02-01 11:54:44', 'TicketStatus', 'ActiveForSupport'		),
		('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2023-02-01 13:54:44', 'TicketStatus', 'Closed'				),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000007', '2024-02-02 11:54:44', 'TicketStatus', 'ActiveForSupport'		),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000007', '2024-02-02 12:15:44', 'TicketStatus', 'ActiveForDevelopers'	),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000007', '2024-02-03 12:54:44', 'FixedInBuild', '1.1.1'					)

--scworkflow_Tickets--
CREATE TABLE  [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets (
	EntityOid			UNIQUEIDENTIFIER,
	AuditAction			INT,
	Modified			DATETIME,
	ChangedProperties	VARCHAR(20) DEFAULT 'EntityType',
	EntityType			INT
)

INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].scworkflow_Tickets
VALUES	('00000000-0000-0000-0000-000000000007', 1, '2023-02-02 13:54:44', 'EntityType', 2)
GO


USE DXStatisticsV2
GO

CREATE OR ALTER FUNCTION dbo.get_ticket_tribes(@ticket_id UNIQUEIDENTIFIER, @ticket_type TINYINT = NULL, @priority_tribe_id UNIQUEIDENTIFIER = NULL)
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

DECLARE @lsc                    TINYINT = 7
DECLARE @devexpress_tribe_id    UNIQUEIDENTIFIER = '340E06F5-9B98-4923-97A4-CA02BA73F075'

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
                        SELECT @devexpress_tribe_id, @least_suitable
                    ) AS ti
                ) AS tribes_inner
        WHERE id IS NOT NULL AND suitability = max_suitability)
RETURN 
END
GO

--TicketsTents--
CREATE TABLE TicketsTents(
	Ticket_Id	UNIQUEIDENTIFIER,
	id			UNIQUEIDENTIFIER,
	name		VARCHAR(20)
)
INSERT INTO TicketsTents
VALUES	('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', 'tent1'),
		('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000004', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000001', 'tent1'),
		('00000000-0000-0000-0000-000000000006', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000007', '00000000-0000-0000-0000-000000000003', 'tent3'),
		('00000000-0000-0000-0000-000000000008', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000009', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000010', '00000000-0000-0000-0000-000000000001', 'tent1'),
		('00000000-0000-0000-0000-000000000011', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000012', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000013', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000014', '00000000-0000-0000-0000-000000000001', 'tent1'),
		('00000000-0000-0000-0000-000000000015', '00000000-0000-0000-0000-000000000002', 'tent2'),
		('00000000-0000-0000-0000-000000000016', '00000000-0000-0000-0000-000000000003', 'tent3')
GO

CREATE OR ALTER FUNCTION dbo.get_ticket_tent(@ticket_id UNIQUEIDENTIFIER)RETURNS TABLE AS
RETURN (
    SELECT TOP 1 id, name
    FROM	TicketsTents
    WHERE  Ticket_Id = @ticket_id
)
GO

PRINT 'test db: up'