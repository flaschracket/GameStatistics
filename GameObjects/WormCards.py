from random import randrange
import copy
from GameObjects.GameSettings import *
from GameObjects.MainRAMVars import *
from GameObjects.Cards import *
from collections import Counter


class WormCards(Cards):
    """description of class"""

    def __init__(self,vars,wcdeck):
        self.PV = copy.deepcopy(vars)
#        self.playedWC = pwc
        self.playedWCName = set()    
        self.damages = []
        self.GS = GameSettings()        
        self.currentWC = 0
        #self.nOfWC = 0
        self.playingdeck =wcdeck
        
        if len(self.playingdeck)==0:
            cards  = [self.GS.WC_BadLuck,self.GS.WC_Normal,self.GS.WC_Week]
            q    = [1,10,5]
            Cards.__init__(self, cardsVaraity = cards, quantities =  q )
            self.shuffle()
            self.playingdeck = self.deck

        #self.WCPlayedcollection = Counter(plyColl)
        #self.reservedWCcollection = Counter(resColl)
        #print(str(self.WCPlayedcollection))
        return 

    def updateWC(self,vars,pwc):
        self.PV = copy.deepcopy(vars)
        playedWC =pwc
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
    #------------------
    def selectWCfromCollection(self):
        self.resetCollection()
        condition = True
        while condition:  
            myWC = randrange(self.GS.NrOfWC)
            if (self.WCPlayedcollection[myWC] < self.GS.WCCollection[myWC]):
                condition = False
                self.currentWC = myWC
                self.WCPlayedcollection[myWC] += 1
                #reserved
        return self
   
    def resetCollection(self):
        diffWC = Counter(self.GS.WCCollection) - self.WCPlayedcollection
        #print(str(diffWC))
        if len(diffWC) == 0 :
            self.WCPlayedcollection = Counter(self.GS.WCPlayedCollection)
            self.WCPlayedcollection = self.WCPlayedcollection + Counter(self.reservedWCcollection)
        return self

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


    def playFunc(self,s):
        self.updateWC(s.P.playerVars,s.playedWC)
        #self.SelectNextWC()
        self.selectWCfromCollection()
        FuncName = 'WCFunc' + str(self.currentWC)
        getattr(self, FuncName)()
        s.P.updatePlayer(self.PV)
        if (len(self.damages) > 0) and (self.damages[0] not in s.P.PCStatus):
            s.P.PCStatus = s.P.PCStatus+self.damages
        return self

    # list of Cards
    #A=Null
    def WCFunc0(self):
        self.playedWCName.add(' WC Name: A=NULL; ')
        #A = 0
        if 0 not in self.PV.Nullindex:
            self.PV.Nullindex.append(0) 
        return(self)
    
    def WCFunc1(self):
        self.playedWCName.add(' WC Name: B=NULL; ')
        if 1 not in self.PV.Nullindex:
            self.PV.Nullindex.append(1) 
        return(self)
    def WCFunc2(self):
        self.playedWCName.add(' WC Name: C=NULL; ')
        if 2 not in self.PV.Nullindex:    
            self.PV.Nullindex.append(2) 
        return(self)

    def WCFunc3(self):
        self.playedWCName.add(' WC Name: B,C=0; ')
        self.assignVar(1,0)
        self.assignVar(2,0)
        return(self)

    def WCFunc4(self):
        self.playedWCName.add(' WC Name: T -=100 ')
        ind= [3]
        if self.ifPossibleToPlay(ind):
            self.PV.varsValue[3] = self.PV.varsValue[3]-100 
     
        return(self)

    def WCFunc5(self):
        self.playedWCName.add(' WC Name: Capture CPU ')
        self.damages.append('CPU1Captured') 
        return(self)
 
    def WCFunc6(self):
        self.playedWCName.add(' WC Name: T =xx00 ')
        ind= [3]
        if self.ifPossibleToPlay(ind):
            mod = self.PV.varsValue[3] % 100
            self.PV.varsValue[3] = self.PV.varsValue[3]-mod 
        return(self)

    def WCFunc7(self):
        self.playedWCName.add(' WC Name: A=0,B=-1,C=N ')
        self.assignVar(0,0)
        self.assignVar(1,-1)
        if 2 not in self.PV.Nullindex:
            self.PV.Nullindex.append(2)
        return(self)

    def WCFunc8(self):
        self.playedWCName.add(' WC Name: B=-10 ')
        self.assignVar(1,-10)
        return(self)

    def WCFunc9(self):
        self.playedWCName.add(' WC Name: C=-20 ')
        self.assignVar(2,-20) 
        return(self)
    def WCFunc10(self):
        self.playedWCName.add(' WC Name: A=0 ')
        self.assignVar(0,0) 
        return(self)
    def WCFunc11(self):
        self.playedWCName.add(' WC Name: B=0 ')
        self.assignVar(1,0) 
        return(self)
    def WCFunc12(self):
        self.playedWCName.add(' WC12: B -=10 ')
        ind= [1]
        if self.ifPossibleToPlay(ind):
            self.PV.varsValue[1] = self.PV.varsValue[1]-10      
        return(self)
    def WCFunc13(self):
        self.playedWCName.add(' WC13: A -=10 ')
        ind= [0]
        if self.ifPossibleToPlay(ind):
            self.PV.varsValue[0] = self.PV.varsValue[0]-10      
        return(self)
    def WCFunc14(self):
        self.playedWCName.add(' WC14: C -=10 ')
        ind= [2]
        if self.ifPossibleToPlay(ind):
            self.PV.varsValue[2] = self.PV.varsValue[2]-10      
        return(self)


    #Bug: when all wcs are played once, and nOfWC is 2, then the game play one WC Card 2 Times instead of playing two WC Card