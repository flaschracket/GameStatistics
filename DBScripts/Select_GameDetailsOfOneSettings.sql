USE [minibit]
GO
/****** Object:  StoredProcedure [dbo].[Select_GamesDetailsofOneSettings]    Script Date: 10/08/2022 17:19:02 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Samira
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
ALTER PROCEDURE [dbo].[Select_GamesDetailsofOneSettings] 
@gamesettingsID int
AS
BEGIN
select step.player,varA,varB,varC,Nulllist,step.total,ECname,WCName,
PCStatus,playerfuncsnames,Step.ReservedEC,Step.RemainedQuantityECset,step.playerfuncs,step.buyDesicions,step.Hardware,step.GameID,cast(roundnr as int) as Roundn,
cast(stepnr as int) as Stepnr, playerfuncs,step.playerdecision as allowedToPlay
,step.ec,Step.WC
from game inner join step 
on GameID = game.ID
where GameSettingsID = @gamesettingsID
--and  nofworms = 2
order by step.GameID,Roundn,Stepnr

END
