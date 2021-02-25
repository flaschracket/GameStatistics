from random import randrange
import copy
from GameObjects.GameSettings import *
from GameObjects.MainRAMVars import *



class WormCards():
    """description of class"""
    const = GameSettings()
    #PV = MainRAMVars()
    
    playedWC = set()
    currentWC = 0
    playedWCName = set()
    nOfWC = 0
    damages = []

    def __init__(self,vars):
        self.PV = copy.deepcopy(vars)
        return 
    #------------------
    def SelectNextWC(self):
        self.reset()
        if len(self.playedWC)==0:
            self.playedWC = {self.currentWC}
        else:
            while self.currentWC in self.playedWC:
                self.currentWC = randrange(self.const.NrOfWC)        
            self.playedWC.add(self.currentWC)        
        return self.currentWC
    
    def reset(self):
        if (len(self.playedWC) == self.const.NrOfWC):
            self.playedWC.clear()
        return(self)

    def playFunc(self):
        self.SelectNextWC()
        FuncName = 'WCFunc' + str(self.currentWC)
        getattr(self, FuncName)()
        return self

    # list of Cards
    #A=Null
    def WCFunc0(self):
        self.playedWCName.add(' WC Name: A=NULL; ')
        self.PV.Nullindex.append(0) 
        return(self)
    
    def WCFunc1(self):
        self.playedWCName.add(' WC Name: B=NULL; ')
        self.PV.Nullindex.append(1) 
        return(self)
    def WCFunc2(self):
        self.playedWCName.add(' WC Name: C=NULL; ')
        self.PV.Nullindex.append(2) 
        return(self)

    def WCFunc3(self):
        self.playedWCName.add(' WC Name: B,C=0; ')
        self.PV.varsValue[1] = 0 
        self.PV.varsValue[2] = 0 
        return(self)

    def WCFunc4(self):
        self.playedWCName.add(' WC Name: T -=100 ')
        self.PV.varsValue[3] = self.PV.varsValue[3]-100 
     
        return(self)

    def WCFunc5(self):
        self.damages.append('CPU1Captured') 
        return(self)
 
    def WCFunc6(self):
        self.playedWCName.add(' WC Name: T =xx00 ')
        mod = self.PV.varsValue[3] % 100
        self.PV.varsValue[3] = self.PV.varsValue[3]-mod 
        return(self)

    def WCFunc7(self):
        self.playedWCName.add(' WC Name: A=0,B=-1,C=N ')
        self.PV.varsValue[0] = 0
        self.PV.varsValue[1] = -1
        self.PV.Nullindex.append(2)
        return(self)

    def WCFunc8(self):
        self.playedWCName.add(' WC Name: B=-10 ')
        self.PV.varsValue[1] = -10 
        return(self)

    def WCFunc9(self):
        self.playedWCName.add(' WC Name: C=-20 ')
        self.PV.varsValue[2] = -20 
        return(self)


    #Bug: when all wcs are played once, and nOfWC is 2, then the game play one WC Card 2 Times instead of playing two WC Card