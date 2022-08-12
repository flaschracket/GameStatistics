USE [minibit]
GO

INSERT INTO [dbo].[Cards]
           ([ID]
           ,[Cardname]
           ,[FunctionNumber]
           ,[Type]
           ,[WCQuantity])
     VALUES
           (<ID, int,>
           ,<Cardname, nvarchar(100),>
           ,<FunctionNumber, int,>
           ,<Type, int,>
           ,<WCQuantity, int,>)
GO

