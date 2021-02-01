from enum import Enum
class GameSettings():
    winGoal = 100
    NrofEC = 5
    NrOfWC = 5
    
    
    
    GameResourceType = Enum('GameResourceType','Hardware EventCard Variable')
    ResourceEventCard = Enum('GameEventCard','Bazar Freelancer Restart')
    ResourceEC = Enum('ResourceEC','Restart Freelancer Bazar')
    TaskEC = Enum('TaskEC','Add1 Add2')
    
    def _init_(self):
        return self
    class GameHardware(Enum): 
        MainRAM = 0
        ExtraRAM = 1
        CPU1 = 2
        CPU2 = 3
        SSD = 4

    @property
    def primary_PC(self):
        return self.MainRAM, self.CPU1


