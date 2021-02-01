#from enum import Enum
from random import randrange
import copy
#from GameObjects.Player import *
from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *

class EventCards():
    """description of class"""
    const = GameSettings()
    PV = MainRAMVars()
    playedCardsSet = set()
    currentEC = 0
    nOfWC= 0

    def SelectNextEC(self):
        self.reset()
        if len(self.playedCardsSet)==0:
            self.playedCardsSet = {self.currentEC}
        else:
            while self.currentEC in self.playedCardsSet:
                self.currentEC = randrange(self.const.NrofEC)        
            self.playedCardsSet.add(self.currentEC)
        
        return self.currentEC
    
    def reset(self):
        #self.sumPlayedEC = self.sumPlayedEC+1
        if (len(self.playedCardsSet) == self.const.NrofEC):
            #self.sumPlayedEC = 0
            self.playedCardsSet.clear()
        return(self)



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
    

