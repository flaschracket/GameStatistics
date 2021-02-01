from random import randrange
import copy
from GameObjects.GameSettings import *
from GameObjects.MainRAMVars import *



class WormCards():
    """description of class"""
    const = GameSettings()
    PV = MainRAMVars()
    playedWormCardsSet = set()
    #currentWormSet = {}
    currentWC = 0
    nOfWC = 0

    def SelectNextWC(self):
        self.reset()
        if len(self.playedWormCardsSet)==0:
            self.playedWormCardsSet = {self.currentWC}
        else:
            while self.currentWC in self.playedWormCardsSet:
                self.currentWC = randrange(self.const.NrOfWC)        
            self.playedWormCardsSet.add(self.currentWC)        
        return self.currentWC
    
    def reset(self):
        if (len(self.playedWormCardsSet) == self.const.NrOfWC):
            self.playedWormCardsSet.clear()
        return(self)



    # list of Cards
    def WCFunc0(self):
        self.PV.VarA = 0 
        return(self)
    def WCFunc1(self):
        self.PV.VarB = -1 
        return(self)
    def WCFunc2(self):
        self.PV.VarC = 0 
        return(self)
    def WCFunc3(self):
        self.PV.VarA = -10 
        return(self)
    def WCFunc4(self):
        self.PV.VarA = 0 
        return(self)
    def WCFunc5(self):
        self.PV.VarA = 0 
        return(self)
 


    #Bug: when all wcs are played once, and nOfWC is 2, then the game play one WC Card 2 Times instead of playing two WC Card