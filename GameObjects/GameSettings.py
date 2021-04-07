from enum import Enum
class GameSettings():
    sampleDataNumber = 1
    winGoal = 100
    #it should be one more of last function number because the functions name are begining with number 0
    NrofEC = 11
    #35
    NrOfWC = 10
    NrOfP = 2
    StoponThisRound = 40
    pauseplayingcount = 2

    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']
    ECCollections = {0:1,1:3,2:5,3:4,4:1,5:1,6:1,7:1,8:1,9:1,10:1}
    ECPlayedCollections = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}

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
        
