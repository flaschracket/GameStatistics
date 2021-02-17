from enum import Enum
class GameSettings():
    winGoal = 100
    NrofEC = 9
    NrOfWC = 5
    resourceECtypes = ['Restart','Bazar','Freelancer']
    #hardwareTypes = ['CPU1','CPU2','RAM1','RAM2', 'SSD'] 
    #functionTypes = ['']
    PCstatus = ['shutdown', 'CPU1Captured', '']
    def _init_(self):
        return self
    def makeRandomDecision(self):
        a = randrange(1000) % 2
        if a == 0:
            return True
        return False
#------------------
#----------------
    
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
        
