from enum import Enum
from random import randrange
import copy
from GameObjects.Player import *
from GameObjects.MainRAMVars import *


class EventCards():
    """description of class"""
    totalEventCards = 5
    sumPlayedEC = 0
    const = GameSettings()
    myrange = 5
    PV = MainRAMVars()
    #EventCardType = Enum('EventCardType','ResourceEC WormEC TaskEC InputEC')
    playedCardsSet = set()
    currentEC = 0

    def SelectEC(self):
        self.reset()
        while self.currentEC in self.playedCardsSet:
            self.currentEC = randrange(self.myrange)        
        self.playedCardsSet.add(self.currentEC)
        return self.currentEC
    
    def reset(self):
        self.sumPlayedEC = self.sumPlayedEC+1
        if (self.sumPlayedEC == self.const.NrofEC):
            self.sumPlayedEC = 0
            self.playedCardsSet.clear()
        return(self)



    # list of Cards
    def ECFunc0(self):
        self.PV.VarA = 5 
        self.currentPenalty = 1
        return(self)

    def ECFunc1(self):
        self.PV.Total = self.PV.Total + self.PV.VarA+ self.PV.VarB + self.PV.VarC+10
        self.currentPenalty = 1
        return(self)
    
    def ECFunc2(self):
        self.PV.VarC = 2  
        self.currentPenalty = 1
        return(self)
    
    def ECFunc3(self):
        self.PV.Total = self.PV.Total + self.PV.VarA+ self.PV.VarB + self.PV.VarC
        self.currentPenalty = 1
        return(self)

    def ECFunc4(self):
        self.PV.VarC = 2  
        self.currentPenalty = 1
        return(self)

    def ECFunc5(self):
        self.PV.VarC = 2  
        self.currentPenalty = 1
        return(self)
    

