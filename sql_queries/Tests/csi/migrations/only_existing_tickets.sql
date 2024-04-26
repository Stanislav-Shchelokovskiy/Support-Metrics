SET NOCOUNT ON
SET ANSI_WARNINGS OFF
:setvar SQLCMDERRORLEVEL 1
GO

CREATE DATABASE SupportCenterPaid
GO
CREATE DATABASE DXStatisticsV2
GO

USE SupportCenterPaid
GO

CREATE SCHEMA [c1f0951c-3885-44cf-accb-1a390f34c342]
GO


CREATE TABLE [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets (
	Id			UNIQUEIDENTIFIER,
	FriendlyId	VARCHAR(20)
);
INSERT INTO [c1f0951c-3885-44cf-accb-1a390f34c342].Tickets
VALUES	('00000000-0000-0000-0000-000000000001', 'ticket1'),
		('00000000-0000-0000-0000-000000000002', 'ticket2')

USE DXStatisticsV2
GO

DECLARE @ticket1 UNIQUEIDENTIFIER = '00000000-0000-0000-0000-000000000001'
DECLARE @ticket2 UNIQUEIDENTIFIER = '00000000-0000-0000-0000-000000000002'
DECLARE @ticket3 UNIQUEIDENTIFIER = '00000000-0000-0000-0000-000000000003'
DECLARE @ticket4 UNIQUEIDENTIFIER = '00000000-0000-0000-0000-000000000004'
DECLARE @ticket5 UNIQUEIDENTIFIER = '00000000-0000-0000-0000-000000000005'

CREATE TABLE FeedbackItems (
	TicketId	UNIQUEIDENTIFIER,
	RatingValue	INT,
	DateTime	DATETIME
)
INSERT INTO FeedbackItems
VALUES	(@ticket5, 1,	'2023-05-01 02:00:00'),
		(@ticket5, 1,	'2023-05-01 02:45:02'),
		(@ticket5, -1,	'2023-05-01 03:20:05'),

		(@ticket1, 1,	'2023-01-01 00:00:00'),
		(@ticket1, 1,	'2023-01-01 00:00:02'),
		(@ticket1, -1,	'2023-01-01 00:00:05'),
		(@ticket1, -1,	'2023-01-01 00:00:07'),
		(@ticket1, -1,	'2023-01-01 00:00:09'),

		(@ticket1, 1,	'2023-01-01 01:00:00'),
		(@ticket1, 0,	'2023-01-01 02:00:02'),
		(@ticket1, 1,	'2023-01-01 02:40:02'),

		(@ticket1, 1,	'2023-01-01 01:00:00'),
		(@ticket1, 1,	'2023-01-01 01:00:02'),
		(@ticket1, 1,	'2023-01-01 01:00:05'),
		(@ticket1, -1,	'2023-01-01 01:00:07'),
		(@ticket1, -1,	'2023-01-01 01:00:09'),

		(@ticket2, -1,	'2023-02-01 01:10:09'),
		(@ticket2, -1,	'2023-02-01 01:05:09'),
		(@ticket2, -1,	'2023-02-01 02:06:00'),
		(@ticket2, 0,	'2023-02-01 05:04:07'),
		(@ticket2, 0,	'2023-02-01 06:05:09'),
		(@ticket2, 0,	'2023-02-01 07:15:09'),

		(@ticket3, 1,	'2023-03-01 01:10:09'),
		(@ticket3, 1,	'2023-03-01 01:05:09'),
		(@ticket3, 1,	'2023-03-01 02:06:00'),
		(@ticket3, 0,	'2023-03-01 05:04:07'),
		(@ticket3, 0,	'2023-03-01 06:05:09'),
		(@ticket3, 0,	'2023-03-01 06:35:10'),

		(@ticket4, -1,	'2023-04-01 00:00:00'),
		(@ticket4, -1,	'2023-04-01 00:00:02'),
		(@ticket4, 1,	'2023-04-01 00:00:05'),
		(@ticket4, 1,	'2023-04-01 00:00:07'),
		(@ticket4, 1,	'2023-04-01 00:00:09'),

		(@ticket4, -1,	'2023-04-01 01:00:00'),
		(@ticket4, 0,	'2023-04-01 02:00:02'),
		(@ticket4, -1,	'2023-04-01 02:40:02'),

		(@ticket4, -1,	'2023-04-01 01:00:00'),
		(@ticket4, -1,	'2023-04-01 01:00:02'),
		(@ticket4, -1,	'2023-04-01 01:00:05'),
		(@ticket4, 1,	'2023-04-01 01:00:07'),
		(@ticket4, 1,	'2023-04-01 01:00:09')
GO

PRINT 'test db: up'