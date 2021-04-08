from enum import Enum
class GameSettings():
    sampleDataNumber = 100
    winGoal = 100
    #it should be one more of last function number because the functions name are begining with number 0
    NrofEC = 32
    NrOfWC = 10
    NrOfP = 2
    StoponThisRound = 40
    pauseplayingcount = 2

    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']
    ECCollection       = {0:10,1:5,2:8,3:6,4:3,5:2,6:3,7:2,8:3,9:2,10:2,11:2,12:2,13:3,14:2,15:3,16:3,17:2,18:2,19:2,20:3,21:2,22:2,23:2,24:2,25:3,26:2,27:3,28:2,29:5,30:2,31:2}
    ECPlayedCollection = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0}
    WCCollection       = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
    WCPlayedCollection = {0:0,1:10,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}


    def _init_(self):
        return self    
#------------------
#----------------
    def ifWined(self,total):
        wined= False
        if (total >= self.winGoal):
            wined = True
        return wined

    class GameHardware(Enum): 
        MainRAM = 0
        ExtraRAM = 1
        CPU1 = 2
        CPU2 = 3
        SSD = 4

    @property
    def primary_PC(self):
        return self.MainRAM, self.CPU1
    
    class ResourceECTypes(Enum): 
        Restart = 0
        Bazar = 1
        Freelancer = 2
        
