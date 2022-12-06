from random import randrange
import copy
import numpy as np
from GameObjects.GameSettings import *
from GameObjects.MainRAMVars import *
from GameObjects.Cards import *
from collections import Counter


class WormCards(Cards):
    """description of class"""

    #def __init__(self,vars,currentgamedeck,playerFuncs):
    def __init__(self,player):
        self.PV = copy.deepcopy(player.playerVars)
        self.playedWCName = []    
        self.playedwc = np.array([]).astype(int)
        self.nofRoundspausing = 0
        self.damages = []
        self.GS = GameSettings()
        self.currentWC = 0
#        self.GD = currentgamedeck
        #self.playingdeck = currentgamedeck.currentWCdeck
        self.playerFuncs = player.playerFuncs
        return 

    def updateWC(self,vars,pwc):      
        self.PV = copy.deepcopy(vars)
        #self.playingdeck = pwc
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
  
    #-------------------
    #player functions
    #1: zero instead of null
    #2: absolute value
    #3: add instead of reduce
    #4: add instead of assign
    #-------------------



    def playFunc(self,player):
        #self.updateWC(s.P.playerVars,s.WC.playingdeck)
        self.updateWC(player.playerVars, player.playerFuncs)
        #self.selectNextWC()
        FuncName = 'WCFunc' + str(self.currentWC)
        getattr(self, FuncName)()
        self.playedwc = np.append(self.playedwc,self.currentWC)
#        s.P.updatePlayer(self.PV,self.nofRoundspausing,[],self.damages,self.playerFuncs)
        #s.GS.currentWCdeck = self.playingdeck
        return 

    # list of Cards
    #A=Null
    def WCFunc0(self):
        self.playedWCName.append(' WC Name: A=NULL; ')        
        if 0 not in self.PV.Nullindex and 0 not in self.playerFuncs:
            self.PV.varsValue[0] = 0
            self.PV.Nullindex.append(0)         
        #self.checkfuncs()
        return(self)
    
    def WCFunc1(self):
        self.playedWCName.append(' WC Name: B=NULL; ')
        if 1 not in self.PV.Nullindex and 1 not in self.playerFuncs:
            self.PV.varsValue[1] = 0
            self.PV.Nullindex.append(1) 
#        self.checkfuncs()
        return(self)
    
    def WCFunc2(self):
        self.playedWCName.append(' WC Name: C=NULL; ')
        if 2 not in self.PV.Nullindex and 2 not in self.playerFuncs:
            self.PV.varsValue[2] = 0
            self.PV.Nullindex.append(2) 
        #self.checkfuncs()
        return(self)

    def WCFunc3(self):
        self.playedWCName.append(' WC Name: B,C=0; ')
        if 4 not in self.playerFuncs:
            self.assignVar(1,0)
            self.assignVar(2,0)
        return(self)

    def WCFunc4(self):
        self.playedWCName.append(' WC Name: T -=64 ')
        ind= [3]
        if self.ifPossibleToPlay(ind):
            if 3 in self.playerFuncs:
                self.PV.varsValue[3] = self.PV.varsValue[3]+64 
            else:
                self.PV.varsValue[3] = self.PV.varsValue[3]-64
            if 2 in self.playerFuncs:
                self.PV.varsValue[3] = abs(self.PV.varsValue[3])             
        return(self)

    def WCFunc5(self):
        self.playedWCName.append(' WC Name: Capture CPU ')
        self.damages.append('CPU1Captured') 
        self.nofRoundspausing = 2
        return(self)
 
    def WCFunc6(self):
        self.playedWCName.append(' WC Name: T =xx00 ') 
        ind= [3]
        if self.ifPossibleToPlay(ind) and 4 not in self.playerFuncs:
#            mod = self.PV.varsValue[3] % 100
 #           self.PV.varsValue[3] = self.PV.varsValue[3]-mod 
            self.PV.varsValue[3] = 0
        return(self)
    #why the function name is only a=0 but do b=0 as well
    def WCFunc7(self):
        self.playedWCName.append(' WC Name: A=0,C=N ')
        if 4 not in self.playerFuncs:
            self.assignVar(0,0)
            self.assignVar(1,0)
        if 2 not in self.PV.Nullindex and 2 not in self.playerFuncs:
            self.PV.varsValue[2] = 0
            self.PV.Nullindex.append(2)
        #self.checkfuncs()
        return(self)

    
    
    def WCFunc10(self):
        self.playedWCName.append(' WC Name: A=0 ')
        if 4 not in self.playerFuncs:
            self.assignVar(0,0) 
        return(self)
    
    def WCFunc11(self):
        if 4 not in self.playerFuncs:
            self.playedWCName.append(' WC Name: B=0 ')
        self.assignVar(1,0) 
        return(self)

    def WCFunc9(self):
        self.playedWCName.append(' WC Name: A = -6 ')
        temp = -6
        if 2 in self.playerFuncs:
            abs(temp) 
        if 4 in self.playerFuncs:
            temp = temp + self.PV.varsValue[0]

        self.assignVar(0,temp)
        return(self)
    def WCFunc15(self):
        self.playedWCName.append(' WC Name: C= -6 ')
        temp = -6
        if 2 in self.playerFuncs:
            abs(temp) 
        if 4 in self.playerFuncs:
            temp = temp + self.PV.varsValue[2]

        self.assignVar(2,temp) 
        return(self)

    def WCFunc8(self):
        self.playedWCName.append(' WC Name: B= -6 ')
        temp = -6
        if 2 in self.playerFuncs:
            abs(temp) 
        if 4 in self.playerFuncs:
            temp = temp + self.PV.varsValue[1]

        self.assignVar(1,temp)
        return(self)

    def WCFunc12(self):
        self.playedWCName.append(' WC12: B -=3 ')
        ind= [1]
        if self.ifPossibleToPlay(ind):
            if 3 in self.playerFuncs:
                self.PV.varsValue[1] = self.PV.varsValue[1]+3      
            else:
                self.PV.varsValue[1] = self.PV.varsValue[1]-3     
            if 2 in self.playerFuncs:
                self.PV.varsValue[1] = abs(self.PV.varsValue[1]) 
        return(self)
    
    def WCFunc13(self):
        self.playedWCName.append(' WC13: A -=3 ')
        ind= [0]
        if self.ifPossibleToPlay(ind):
            if 3 in self.playerFuncs:
                self.PV.varsValue[0] = self.PV.varsValue[0]+3      
            else:
                self.PV.varsValue[0] = self.PV.varsValue[0]-3          
            if 2 in self.playerFuncs:
                self.PV.varsValue[0] = abs(self.PV.varsValue[0])
        return(self)

    def WCFunc14(self):
        self.playedWCName.append(' WC14: C -=3 ')
        ind= [2]
        if self.ifPossibleToPlay(ind):
            if 3 in self.playerFuncs:
                self.PV.varsValue[2] = self.PV.varsValue[2]+3      
            else:
                self.PV.varsValue[2] = self.PV.varsValue[2]-3     
        if 2 in self.playerFuncs:
                self.PV.varsValue[2] = abs(self.PV.varsValue[2])
        return(self)


    #Bug: when all wcs are played once, and nOfWC is 2, then the game play one WC Card 2 Times instead of playing two WC Card