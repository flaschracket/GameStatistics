from enum import Enum
from random import randrange
import copy
from GameObjects.Player import *
from GameObjects.MainRAMVars import *


class EventCards():
    """description of class"""
    totalEventCards = 10
    myrange = 11
    PV = MainRAMVars()
    #EventCardType = Enum('EventCardType','ResourceEC WormEC TaskEC InputEC')
    playedCardsSet = {0}
    currentEC = 0

    def SelectEC(self):
        while self.currentEC in self.playedCardsSet:
            self.currentEC = randrange(self.myrange)        
        self.playedCardsSet.add(self.currentEC)
        print(self.playedCardsSet)
        return self.currentEC
    
    def Set(self,sumplayedEC):
        sumplayedEC = sumplayedEC +1
        if (sumplayedEC == self.totalEventCards):
        #   print('All EC Cards are played')
            sumplayedEC = 0
            self.playedCardsSet.clear()
        return(sumplayedEC)



    # list of Cards
    def ECFunc0(self, p = Player()):
        p.PlayerVars.VarA = 5 
        p.currentPenalty = 1
        return(p)

    def ECFunc1(self):
        self.PV.Total = self.PV.Total + self.PV.VarA+ self.PV.VarB + self.PV.VarC+10
        currentPenalty = 1
        return(self)
    
    def ECFunc2(self, p= Player()):
        p.PlayerVars.VarC = 2  
        p.currentPenalty = 1
        return(p)
    
    def ECFunc3(self, p= Player()):
        #print("p-f3:" + p.Name)
        PV = copy.deepcopy(p.PlayerVars())
        PV.Total = PV.Total + PV.VarA+ PV.VarB + PV.VarC
        #print("p-f3:" + PV.Total)
        p.currentPenalty = 1
        p.PlayerVars = copy.deepcopy(PV)
        return(p)

    def ECFunc4(self, p= Player()):
        PV = copy.deepcopy(p.PlayerVars())
        PV.Total = PV.Total + PV.VarA+ PV.VarB + PV.VarC
        p.currentPenalty = 1
        return(p)
    
    def ECFunc5(self, p= Player()):
        PV = copy.deepcopy(p.PlayerVars())
        PV.Total = PV.Total + PV.VarA+ PV.VarB + PV.VarC
        p.currentPenalty = 1
        return(p)
    
    def ECFunc6(self):
        PV = copy.deepcopy(p.PlayerVars())
        PV.Total = PV.Total + PV.VarA+ PV.VarB + PV.VarC
        p.currentPenalty = 1
        return(p)
    
    def ECFunc7(self):
        p.currentPenalty = 1
        return(p)
    
    def ECFunc8(self):
        p.currentPenalty = 1
        return(p)
    
    def ECFunc9(self):
        p.currentPenalty = 1
        return(p)

    def ECFunc10(self):
        p.currentPenalty = 1
        return(p)

    def ECFunc11(self):
        p.currentPenalty = 1
        return(p)

