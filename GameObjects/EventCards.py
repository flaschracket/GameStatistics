#from enum import Enum
from random import randrange
import copy
#from GameObjects.Player import *
from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *
#0 to 5 task functions
#6 to 9 input functions
#10 to 30 resource functions
class EventCards():
    """description of class"""
    GS = GameSettings()
    PV = MainRAMVars()
    playedCardsSet = set()
    reservedCardsSet =set()
    
    hardware= []
    # initial which resource is added after playing an EC card
    resourceEC = []
    currentEC = 0
    nOfWC= 0

    def SelectNextEC(self):
        self.reset()
        if len(self.playedCardsSet)==0:
            self.playedCardsSet = {self.currentEC}
        else:
            while ((self.currentEC in self.playedCardsSet) or (self.currentEC in self.reservedCardsSet)):
                self.currentEC = randrange(self.GS.NrofEC)        
            self.playedCardsSet.add(self.currentEC)        
        return self.currentEC
    
    def reset(self):
        #self.sumPlayedEC = self.sumPlayedEC+1
        if (len(self.playedCardsSet) == self.GS.NrofEC):
            self.playedCardsSet.clear()
            self.playedCardsSet = copy.deepcopy(self.reservedCardsSet)
        return(self)
    def unreserve(self,ec):
        self.reservedCardsSet.discard(ec)


    # list of Cards
    def ECFunc0(self):
        self.PV.VarA = 5 
        self.nOfWC = 0
        return(self)

    def ECFunc1(self):
        self.PV.Total = self.PV.Total + self.PV.VarA+ self.PV.VarB + self.PV.VarC+10
        self.nOfWC = 1
        return(self)
    
    def ECFunc2(self):
        self.PV.VarC = 2  
        self.nOfWC = 2
        return(self)
    
    def ECFunc3(self):
        self.PV.Total = self.PV.Total + self.PV.VarA+ self.PV.VarB + self.PV.VarC
        self.nOfWC = 1
        return(self)

    def ECFunc4(self):
        self.PV.VarC = 2  
        self.nOfWC = 2
        return(self)

    def ECFunc5(self):
        self.PV.VarC = 2  
        self.nOfWC = 0
        return(self)
    # input functions 
    def ECFunc6(self):
        self.PV.VarC = 2  
        self.nOfWC = 0
        return(self)
    #resource functions
    def ECFunc7(self):
#        if (self.GS.GameHardware.CPU2 not in self.hardware):
        self.resourceEC.append(self.GS.ResourceECTypes.Restart)
        self.reservedCardsSet.add(7)
        return(self)
    def ECFunc8(self):
        self.resourceEC.append(self.GS.ResourceECTypes.Freelancer)
        self.reservedCardsSet.add(8)
        return(self)
    
    #adding hardware to pc of player
    #def ECFunc9(self):
     #   if (self.GS.GameHardware.SSD not in self.hardware):
      #      self.hardware.append(self.GS.GameHardware.SSD)
       # return(self)
            
