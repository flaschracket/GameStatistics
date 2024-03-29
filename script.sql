USE [master]
GO
/****** Object:  Database [minibit]    Script Date: 02/11/2021 11:09:22 ******/
CREATE DATABASE [minibit]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'minibit', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\minibit.mdf' , SIZE = 204800KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'minibit_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\minibit_log.ldf' , SIZE = 7872512KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [minibit] SET COMPATIBILITY_LEVEL = 140
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [minibit].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [minibit] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [minibit] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [minibit] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [minibit] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [minibit] SET ARITHABORT OFF 
GO
ALTER DATABASE [minibit] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [minibit] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [minibit] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [minibit] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [minibit] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [minibit] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [minibit] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [minibit] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [minibit] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [minibit] SET  DISABLE_BROKER 
GO
ALTER DATABASE [minibit] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [minibit] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [minibit] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [minibit] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [minibit] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [minibit] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [minibit] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [minibit] SET RECOVERY FULL 
GO
ALTER DATABASE [minibit] SET  MULTI_USER 
GO
ALTER DATABASE [minibit] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [minibit] SET DB_CHAINING OFF 
GO
ALTER DATABASE [minibit] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [minibit] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [minibit] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'minibit', N'ON'
GO
ALTER DATABASE [minibit] SET QUERY_STORE = OFF
GO
USE [minibit]
GO
/****** Object:  Table [dbo].[Game]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Game](
	[samplenumber] [nvarchar](50) NULL,
	[winner] [nvarchar](50) NULL,
	[Total] [nvarchar](50) NULL,
	[lastRound] [nvarchar](50) NULL,
	[lastStep] [nvarchar](50) NULL,
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[GameSettingsID] [int] NULL,
 CONSTRAINT [PK_Game] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Step]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Step](
	[GameID] [int] NULL,
	[samplenumber] [int] NULL,
	[roundnr] [nvarchar](50) NULL,
	[stepnr] [nvarchar](50) NULL,
	[player] [nvarchar](50) NULL,
	[varA] [nvarchar](50) NULL,
	[varB] [nvarchar](50) NULL,
	[varC] [nvarchar](50) NULL,
	[total] [nvarchar](50) NULL,
	[ec] [nvarchar](50) NULL,
	[nofworms] [nvarchar](50) NULL,
	[playerdecision] [nvarchar](50) NULL,
	[ECname] [nvarchar](100) NULL,
	[Nulllist] [nvarchar](50) NULL,
	[PCStatus] [nvarchar](100) NULL,
	[WCName] [nvarchar](100) NULL,
	[RemainedQuantityECset] [nvarchar](100) NULL,
	[WCset] [nvarchar](100) NULL,
	[ID] [int] IDENTITY(1,1) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[Games]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[Games]
AS
SELECT TOP (100) PERCENT dbo.Step.samplenumber, CAST(dbo.Step.stepnr AS int) AS row, dbo.Step.roundnr, dbo.Step.stepnr, dbo.Step.player, dbo.Step.varA, dbo.Step.varB, dbo.Step.varC, dbo.Step.total, dbo.Step.ec, dbo.Step.nofworms, 
                  dbo.Step.playerdecision, dbo.Step.ECname, dbo.Game.winner, dbo.Game.Total AS [winer Total value], dbo.Game.samplenumber AS samplenr, dbo.Step.Nulllist, dbo.Step.PCStatus, dbo.Step.WCName, dbo.Step.playedECset, 
                  dbo.Step.playedWCset, dbo.Game.ID, dbo.Game.lastStep, dbo.Game.lastRound, dbo.Step.GameID, dbo.Game.GameSettingsID
FROM     dbo.Game INNER JOIN
                  dbo.Step ON dbo.Game.samplenumber = dbo.Step.samplenumber AND dbo.Step.GameID = dbo.Game.ID
ORDER BY samplenr, row
GO
/****** Object:  View [dbo].[winnedGames]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[winnedGames]
AS
SELECT samplenumber, row, roundnr, stepnr, player, varA, varB, varC, total, ec, nofworms, playerdecision, ECname, winner, [winer Total value], samplenr, Nulllist, PCStatus, WCName, playedECset, playedWCset, ID, lastStep, lastRound, GameID, 
                  GameSettingsID
FROM     dbo.Games
WHERE  (GameID IN
                      (SELECT ID
                       FROM      dbo.Game
                       WHERE   (Total >= 100)))
GO
/****** Object:  View [dbo].[Games_Abundance_EC]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[Games_Abundance_EC]
AS
SELECT TOP (100) PERCENT ec, COUNT(ec) AS NrOfEC, GameSettingsID
FROM     dbo.winnedGames
GROUP BY ec, GameSettingsID
ORDER BY NrOfEC
GO
/****** Object:  View [dbo].[Games_WC_Abundance]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[Games_WC_Abundance]
AS
SELECT TOP (100) PERCENT GameSettingsID, playedWCset, COUNT(playedWCset) AS NrOfWC
FROM     dbo.winnedGames
GROUP BY GameSettingsID, playedWCset
ORDER BY NrOfWC
GO
/****** Object:  Table [dbo].[Cards]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cards](
	[ID] [int] NOT NULL,
	[Cardname] [nvarchar](100) NULL,
	[FunctionNumber] [int] NULL,
	[Type] [int] NULL,
	[WCQuantity] [int] NOT NULL,
 CONSTRAINT [PK_Cards] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Category]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Category](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](100) NULL,
	[Quantity] [int] NOT NULL,
	[typenumber] [int] NULL,
 CONSTRAINT [PK_Card Effect] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CardCategory]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CardCategory](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[CardID] [int] NULL,
	[CategoryID] [int] NULL,
 CONSTRAINT [PK_CardCategorie] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[list of cards]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[list of cards]
AS
SELECT TOP (100) PERCENT dbo.Category.Name AS categoryname, dbo.Cards.Cardname, dbo.Cards.FunctionNumber, dbo.Category.Quantity AS RepeatQuantity, dbo.Category.ID AS CategoryID, dbo.Cards.ID AS CardsID, 
                  dbo.CardCategory.ID AS CardCategoryID
FROM     dbo.CardCategory INNER JOIN
                  dbo.Cards ON dbo.CardCategory.CardID = dbo.Cards.ID INNER JOIN
                  dbo.Category ON dbo.CardCategory.CategoryID = dbo.Category.ID
GO
/****** Object:  View [dbo].[TotalStatistics]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[TotalStatistics]
AS
SELECT Total, COUNT(Total) AS count
FROM     dbo.Game
GROUP BY Total
GO
/****** Object:  View [dbo].[Wined games_Abundance_EC]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[Wined games_Abundance_EC]
AS
SELECT TOP (100) PERCENT ec, COUNT(ec) AS NrOfEC, GameSettingsID
FROM     dbo.winnedGames
GROUP BY ec, GameSettingsID
ORDER BY NrOfEC
GO
/****** Object:  Table [dbo].[GameReport]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[GameReport](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[towtimestotal] [int] NULL,
	[games] [int] NULL,
	[onequarterroundTowtimestotal] [int] NULL,
	[winners] [int] NULL,
	[FirstGameID] [int] NULL,
	[LastGameID] [int] NULL,
	[changelog] [nvarchar](max) NULL,
	[onequarterrounds] [int] NULL,
 CONSTRAINT [PK_GameReport] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[GameSettings]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[GameSettings](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[ChangeLog] [nvarchar](max) NULL,
	[SampleQuantity] [int] NULL,
	[winGoal] [int] NULL,
	[players] [int] NULL,
	[MaxRound] [int] NULL,
	[EC_Types] [nvarchar](max) NULL,
	[EC_Q_T] [nvarchar](max) NULL,
	[EC_TotalQ] [int] NULL,
	[WC_Types] [nvarchar](max) NULL,
	[WC_Q_T] [nvarchar](max) NULL,
	[WC_TotalQ] [int] NULL,
	[FirstDeck] [nvarchar](max) NULL,
 CONSTRAINT [PK_GameSettings] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player](
	[playername] [nvarchar](50) NULL,
	[ID] [int] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Cards] ADD  CONSTRAINT [DF_Cards_WCQuantity]  DEFAULT ((0)) FOR [WCQuantity]
GO
ALTER TABLE [dbo].[Category] ADD  CONSTRAINT [DF_Category_Quantity]  DEFAULT ((0)) FOR [Quantity]
GO
ALTER TABLE [dbo].[CardCategory]  WITH CHECK ADD  CONSTRAINT [FK_CardCategorie_Cards] FOREIGN KEY([CardID])
REFERENCES [dbo].[Cards] ([ID])
GO
ALTER TABLE [dbo].[CardCategory] CHECK CONSTRAINT [FK_CardCategorie_Cards]
GO
ALTER TABLE [dbo].[CardCategory]  WITH CHECK ADD  CONSTRAINT [FK_CardCategorie_Category] FOREIGN KEY([CategoryID])
REFERENCES [dbo].[Category] ([ID])
GO
ALTER TABLE [dbo].[CardCategory] CHECK CONSTRAINT [FK_CardCategorie_Category]
GO
ALTER TABLE [dbo].[Game]  WITH CHECK ADD  CONSTRAINT [FK_Game_GameSettings] FOREIGN KEY([GameSettingsID])
REFERENCES [dbo].[GameSettings] ([ID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Game] CHECK CONSTRAINT [FK_Game_GameSettings]
GO
ALTER TABLE [dbo].[Step]  WITH CHECK ADD  CONSTRAINT [FK_Step_Game] FOREIGN KEY([GameID])
REFERENCES [dbo].[Game] ([ID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Step] CHECK CONSTRAINT [FK_Step_Game]
GO
/****** Object:  StoredProcedure [dbo].[fill_GameReport_FromID]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[fill_GameReport_FromID]
@fromGamesettingsID int
AS
BEGIN
---------------
--vars
----------------------------
declare @rounds10m  int;
declare @total200p  int;
declare @games  int;
declare @round_total int;
declare @winners int;
declare @firstID int;
declare @lastID int;
declare @ids table(idx int identity(1,1), lastID int)
declare @i int
declare @max int
declare @wingoal int
declare @maxround int
declare @log nvarchar(MAX)

declare @temptable table(samplenumber nvarchar(50),winner nvarchar(50),Total nvarchar(50),lastRound nvarchar(50),lastStep nvarchar(50),ID int,gamesettingsid int)

---------------------------
-- table of last ID of each series of samplegame
---------------------------
insert into @ids (lastID)
select  min(ID)-1 from game where GameSettingsID = @fromGamesettingsID
union
select MAX(ID) lastID from game
where GameSettingsID>= @fromGamesettingsID
group by GameSettingsID

----------------------
-- fill vars before while
------------------------
select @Max = count(idx) from @ids
set @i = 1
----------------------------
-- make desire data of each series and save in DB-dbo.GameReport
-----------------------------
while @i < @max

begin
------------
-- selecting a serie
------------
select @firstID=lastID from @ids where idx=@i
select @lastID=lastID from @ids where idx=@i+1
select @log =  changelog from GameSettings join game on gamesettings.id = game.gamesettingsID where game.ID = @lastID
select @wingoal =  winGoal,@maxround=MaxRound from GameSettings join game on gamesettings.id = game.gamesettingsID where game.ID = @lastID
insert into @temptable
select  * from game where 	(ID >= @firstID)	and 	(ID<= @lastID)
--------------
--making data out of a serie
--------------
select @rounds10m = (select count(ID)  from @temptable where lastRound<(@maxround/4));

select  @total200p = count(Total) from @temptable where Total >(@wingoal * 2);
   
select  @games = count(ID)  from @temptable;

select @round_total = count(total) from @temptable where lastRound<(@maxround/4) and total >(@wingoal * 2);

select @winners = count(ID) from @temptable where total >= @wingoal
-------------
--insert
-------------
insert into dbo.GameReport
select @total200p,@games,@round_total, @winners,@firstID, @lastID,@log,@rounds10m 
----------------
--prepare for next round
----------------
set @i = @i+1

delete from @temptable

end


END
GO
/****** Object:  StoredProcedure [dbo].[gamesLessthan]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[gamesLessthan]
@Round int,
@GameID int
AS
BEGIN

select * from step 
where GameID in (select ID from game 
where lastRound <@Round
and gameID > @GameID
)
order by samplenumber,cast(stepnr as int)

END
GO
/****** Object:  StoredProcedure [dbo].[NotEndedGames]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[NotEndedGames]
@GIDfrom int,
@GIDto int

AS
BEGIN
select * from step where GameID in (select ID from Game where ID>=@GIDfrom and ID<=@GIDto and winner = '')
order by GameID, cast(stepnr as int)
END
GO
/****** Object:  StoredProcedure [dbo].[playersequence]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[playersequence] 
	-- Add the parameters for the stored procedure here
@playername nvarchar(100),
@GameID  int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

select * from step
where GameID = @GameID
and player = @playername
order by cast(roundnr as int)
return

END
GO
/****** Object:  StoredProcedure [dbo].[queresImade]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[queresImade]
AS
BEGIN
  select lastRound, count(lastRound) as redundency from game
  group by lastRound

select * from (
SELECT TOP (1000) [Total]
      ,[count]
  FROM [minibit].[dbo].[TotalStatistics]) as A
  where Total >99

  select count(lastRound) as RoundNumberslessthan10, sum(redundency) as plays from (select lastRound, count(lastRound) as redundency from game
  group by lastRound)  as A
  where lastRound <10


END
GO
/****** Object:  StoredProcedure [dbo].[Select_GamesDetailsofOneSettings]    Script Date: 02/11/2021 11:09:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Samira
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Select_GamesDetailsofOneSettings] 
@gamesettingsID int
AS
BEGIN
select step.player,step.playerdecision,varA,varB,varC,Nulllist,step.total,ECname,nofworms,WCName,step.ec,
PCStatus,Step.WCset,Step.RemainedQuantityECset,step.GameID,cast(roundnr as int) as Roundn,cast(stepnr as int) as Stepnr
from game inner join step 
on GameID = game.ID
where GameSettingsID = @gamesettingsID
--and  nofworms = 2
order by step.GameID,Roundn,Stepnr

END
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'list of WC numbers which are played in this step' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Step', @level2type=N'COLUMN',@level2name=N'WCset'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[22] 4[39] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = -120
         Left = 0
      End
      Begin Tables = 
         Begin Table = "Game"
            Begin Extent = 
               Top = 7
               Left = 48
               Bottom = 235
               Right = 242
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "Step"
            Begin Extent = 
               Top = 0
               Left = 437
               Bottom = 163
               Right = 631
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 2508
         Alias = 900
         Table = 1176
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1356
         SortOrder = 1416
         GroupBy = 1350
         Filter = 1356
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Games'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Games'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "winnedGames"
            Begin Extent = 
               Top = 7
               Left = 48
               Bottom = 170
               Right = 256
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 12
         Column = 1440
         Alias = 900
         Table = 1176
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1356
         SortOrder = 1416
         GroupBy = 1350
         Filter = 1356
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Games_Abundance_EC'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Games_Abundance_EC'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "winnedGames"
            Begin Extent = 
               Top = 7
               Left = 48
               Bottom = 310
               Right = 256
            End
            DisplayFlags = 280
            TopColumn = 16
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 12
         Column = 1488
         Alias = 900
         Table = 1176
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1356
         SortOrder = 1416
         GroupBy = 1350
         Filter = 1356
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Games_WC_Abundance'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Games_WC_Abundance'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[41] 4[36] 2[5] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "CardCategory"
            Begin Extent = 
               Top = 30
               Left = 300
               Bottom = 202
               Right = 494
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "Cards"
            Begin Extent = 
               Top = 136
               Left = 79
               Bottom = 299
               Right = 284
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "Category"
            Begin Extent = 
               Top = 89
               Left = 759
               Bottom = 230
               Right = 953
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
      Begin ColumnWidths = 9
         Width = 284
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 1656
         Table = 1176
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1356
         SortOrder = 1416
         GroupBy = 1350
         Filter = 1356
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'list of cards'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'list of cards'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[41] 4[20] 2[9] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "Game"
            Begin Extent = 
               Top = 7
               Left = 48
               Bottom = 170
               Right = 242
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
      Begin ColumnWidths = 9
         Width = 284
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 12
         Column = 1440
         Alias = 900
         Table = 1176
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1356
         SortOrder = 1416
         GroupBy = 1350
         Filter = 1356
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'TotalStatistics'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'TotalStatistics'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "winnedGames"
            Begin Extent = 
               Top = 7
               Left = 48
               Bottom = 310
               Right = 272
            End
            DisplayFlags = 280
            TopColumn = 6
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
      Begin ColumnWidths = 9
         Width = 284
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 12
         Column = 1440
         Alias = 900
         Table = 1176
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1356
         SortOrder = 1416
         GroupBy = 1350
         Filter = 1356
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Wined games_Abundance_EC'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'Wined games_Abundance_EC'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = -5640
         Left = 0
      End
      Begin Tables = 
         Begin Table = "Games"
            Begin Extent = 
               Top = 7
               Left = 48
               Bottom = 170
               Right = 256
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
      Begin ColumnWidths = 9
         Width = 284
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
         Width = 1200
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 900
         Table = 1176
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1356
         SortOrder = 1416
         GroupBy = 1350
         Filter = 1356
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'winnedGames'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'winnedGames'
GO
USE [master]
GO
ALTER DATABASE [minibit] SET  READ_WRITE 
GO
