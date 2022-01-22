from random import randrange
import copy
import numpy as np
from GameObjects.GameSettings import *
from GameObjects.MainRAMVars import *
from GameObjects.Cards import *
from collections import Counter


class WormCards(Cards):
    """description of class"""

    def __init__(self,vars,currentgamedeck,playerfuncs):
        self.PV = copy.deepcopy(vars)
        self.playedWCName = []    
        self.playedwc = np.array([]).astype(int)
        self.nofRoundspausing = 0
        self.damages = []
        self.GS = GameSettings()
        self.currentWC = 0
        self.GD = currentgamedeck
        self.playingdeck = currentgamedeck.currentWCdeck
        self.playerfuncs = playerfuncs
        return 

    def updateWC(self,vars,pwc):
        
        self.PV = copy.deepcopy(vars)
        self.playingdeck = pwc
        return self

    def ifPossibleToPlay(self,ind):
        a= any(item in ind for item in self.PV.Nullindex)
        if   a==True:
            return False
        return True

    def assignVar(self,var,value):
        if var in self.PV.Nullindex:
            self.PV.Nullindex.remove(var)
        self.PV.varsValue[var]=value
        return
    def shuffle(self):
        shuffle(self.playingdeck)
    
    def selectNextWC(self):
        self.reset()
        wc = self.playingdeck[0]
        self.currentWC = wc
        self.playingdeck = np.delete(self.playingdeck,[0])
        return self.currentWC
    
    def reset(self):
        if (len(self.playingdeck) == 0):
            self.playingdeck = self.GD.initialWC.deck
            self.shuffle()
        return(self)
    def checkfuncs(self):
        if 1 in self.playerfuncs:
           self.PV.Nullindex.clear
        return 0
    def playFunc(self,s):
        self.updateWC(s.P.playerVars,s.WC.playingdeck)
        #self.selectNextWC()
        FuncName = 'WCFunc' + str(self.currentWC)
        getattr(self, FuncName)()
        self.playedwc = np.append(self.playedwc,self.currentWC)
        s.P.updatePlayer(self.PV,self.nofRoundspausing,[],self.damages,self.playerfuncs)
        #s.GS.currentWCdeck = self.playingdeck
        return s

    # list of Cards
    #A=Null
    def WCFunc0(self):
        self.playedWCName.append(' WC Name: A=NULL; ')        
        if 0 not in self.PV.Nullindex:
            self.PV.varsValue[0] = 0
            self.PV.Nullindex.append(0) 
        self.checkfuncs()
        return(self)
    
    def WCFunc1(self):
        self.playedWCName.append(' WC Name: B=NULL; ')
        if 1 not in self.PV.Nullindex:
            self.PV.varsValue[1] = 0
            self.PV.Nullindex.append(1) 
        self.checkfuncs()
        return(self)
    
    def WCFunc2(self):
        self.playedWCName.append(' WC Name: C=NULL; ')
        if 2 not in self.PV.Nullindex:
            self.PV.varsValue[2] = 0
            self.PV.Nullindex.append(2) 
        self.checkfuncs()
        return(self)

    def WCFunc3(self):
        self.playedWCName.append(' WC Name: B,C=0; ')
        self.assignVar(1,0)
        self.assignVar(2,0)
        return(self)

    def WCFunc4(self):
        self.playedWCName.append(' WC Name: T -=64 ')
        ind= [3]
        if self.ifPossibleToPlay(ind):
            if 2 in self.playerfuncs:
                self.PV.varsValue[3] = self.PV.varsValue[3]+64 
            else:
                self.PV.varsValue[3] = self.PV.varsValue[3]-64
             
        return(self)

    def WCFunc5(self):
        self.playedWCName.append(' WC Name: Capture CPU ')
        self.damages.append('CPU1Captured') 
        self.nofRoundspausing = 2
        return(self)
 
    def WCFunc6(self):
        self.playedWCName.append(' WC Name: T =xx00 ') 
        ind= [3]
        if self.ifPossibleToPlay(ind):
            mod = self.PV.varsValue[3] % 100
            self.PV.varsValue[3] = self.PV.varsValue[3]-mod 
            self.PV.varsValue[3] = 0
        return(self)

    def WCFunc7(self):
        self.playedWCName.append(' WC Name: A=0,C=N ')
        self.assignVar(0,0)
        self.assignVar(1,0)
        if 2 not in self.PV.Nullindex:
            self.PV.varsValue[2] = 0
            self.PV.Nullindex.append(2)
        self.checkfuncs()
        return(self)

    
    
    def WCFunc10(self):
        self.playedWCName.append(' WC Name: A=0 ')
        self.assignVar(0,0) 
        return(self)
    
    def WCFunc11(self):
        self.playedWCName.append(' WC Name: B=0 ')
        self.assignVar(1,0) 
        return(self)

    def WCFunc9(self):
        self.playedWCName.append(' WC Name: A = -6 ')
        if 1 in self.playerfuncs:
            self.assignVar(0,6) 
        else:
            self.assignVar(0,-6)
        return(self)
    def WCFunc15(self):
        self.playedWCName.append(' WC Name: C= -6 ')
        if 1 in self.playerfuncs:
            self.assignVar(2,6) 
        else:
            self.assignVar(2,-6) 
        return(self)

    def WCFunc8(self):
        self.playedWCName.append(' WC Name: B= -6 ')
        if 1 in self.playerfuncs:
            self.assignVar(1,6) 
        else:
            self.assignVar(1,-6)
        return(self)

    def WCFunc12(self):
        self.playedWCName.append(' WC12: B -=3 ')
        ind= [1]
        if self.ifPossibleToPlay(ind):
            if 2 in self.playerfuncs:
                self.PV.varsValue[1] = self.PV.varsValue[1]+3      
            else:
                self.PV.varsValue[1] = self.PV.varsValue[1]-3     
             
        return(self)
    
    def WCFunc13(self):
        self.playedWCName.append(' WC13: A -=3 ')
        ind= [0]
        if self.ifPossibleToPlay(ind):
            if 2 in self.playerfuncs:
                self.PV.varsValue[0] = self.PV.varsValue[0]+3      
            else:
                self.PV.varsValue[0] = self.PV.varsValue[0]-3          
        return(self)

    def WCFunc14(self):
        self.playedWCName.append(' WC14: C -=3 ')
        ind= [2]
        if self.ifPossibleToPlay(ind):
            if 2 in self.playerfuncs:
                self.PV.varsValue[2] = self.PV.varsValue[2]+3      
            else:
                self.PV.varsValue[2] = self.PV.varsValue[2]-3     
        return(self)


    #Bug: when all wcs are played once, and nOfWC is 2, then the game play one WC Card 2 Times instead of playing two WC Card