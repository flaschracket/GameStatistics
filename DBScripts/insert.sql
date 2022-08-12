USE [minibit]
GO

INSERT INTO [dbo].[Bazar]
           ([ID]
           ,[name]
           ,[mainprice]
           ,[sharedprice]
           ,[type])
     VALUES
           (<ID, int,>
           ,<name, nvarchar(100),>
           ,<mainprice, int,>
           ,<sharedprice, int,>
           ,<type, bit,>)
GO

