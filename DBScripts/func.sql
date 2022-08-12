--select * from GameSettings order by ID desc
--select * from game where GameSettingsID = 15833

select playerfuncs, Nulllist,varA,varB,varC,total, player, stepnr, ec,gameID, ID from  (
select playerfuncs, Nulllist,varA,varB,varC,total, player, stepnr,ec,gameID, ID from step 
where GameID in (select ID from game where GameSettingsID = 16823)
and ec = '201' 
--order by ID desc
) as a
union
(select playerfuncs, Nulllist,varA,varB,varC,total, player, stepnr,ec,gameID, ID
from step where ID in (select ID-5 from step where gameID in 
(select ID from game where GameSettingsID = 16823)
and ec = '201' ) 
--order by ID desc
) order by ID asc
--select * from step where gameID = 72874 and (stepnr= 55 or stepnr=60)

--1 does not empty null index
--2 when o is null does not buy function