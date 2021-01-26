from GameObjects.GameSettings import *
from GameObjects.Step import *
from GameObjects.MainRAMVars import *
from GameObjects.Player import *
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from random import randrange
import copy


class Game():
    """description of class"""
    winer = ''
#    sumplayedEC = 0 
    nofPlayers = 0
    nOfCorruption = 0
    currentRound = 0
    currentEC = 0
    currentWormsSet = {}
    currentStep = 0
    currentPenalty = 0
    currentPlayer = Player()
    listofPlayers = []
    listofSteps = []
    EC = EventCards()
    WC = WormCards()
    DE = GameSettings()
    

    

    def ifWined(self):
        wined= False
        #print("check winer:" + self.currentPlayer.Name)
        if (self.currentPlayer.PlayerVars.Total > self.DE.winGoal):
            wined = True
            self.winer = self.currentPlayer.Name
        #print("winer:" + self.winer)
        return (self)
    
    def playEC(self):
        """calling a function with making its name as string"""
        self.currentEC = self.EC.SelectEC()
        self.EC.PV = copy.deepcopy(self.currentPlayer.PlayerVars)
        FuncName = 'ECFunc' + str(self.currentEC)
        getattr(self.EC, FuncName)()
        self.currentPlayer.PlayerVars = copy.deepcopy(self.EC.PV)
        return(self)

    def playWC(self):
        self.currentWC = self.WC.selectWC()
        FuncName = 'WCFunc' + str(self.currentWC)
        funcresult = getattr(self.WC, FuncName)()
        #OMGCorruption(self,myturn)
        return True

    def playOneStep(self):
        self.currentStep = self.currentStep+1
        self.playEC()
        self.ifWined()
        if (self.winer != ''):
            s = copy.deepcopy(self.Stepsnapshot())    
            return (self)
        self.EC.playedCardsSet.add(self.currentEC)
        for i in range(self.nOfCorruption):
            self.playWC()
        self.listofSteps.append(self.Stepsnapshot())
        self.listofSteps[self.currentStep].printCSV()
        return (self)
    
    def playOneRound(self):
        for x in range(self.nofPlayers):
            #print("round is:"+str(x))
            #print(self.listofPlayers[x].Name)
            self.currentPlayer = copy.deepcopy(self.listofPlayers[x])
            #print(self.currentPlayer.Name)
            #self.currentPlayer.printMainRAM()
            #self.listofPlayers[x].printMainRAM()
            self.EC.reset()
            #self.printgame("round:")
            self.playOneStep()
            #print("t in r="+ str(self.currentPlayer.PlayerVars.Total))             
            self.listofPlayers[x] = copy.deepcopy(self.currentPlayer)
            #print("palyer: "+ self.currentPlayer.Name)
            #print("t in list="+ str(self.listofPlayers[x].PlayerVars.Total))
            #print("winer"+self.winer)
            if (self.winer != ''):
                break            
        return self

    def Stepsnapshot(self):
        s = Step()
        s.roundNr = self.currentRound
        s.stepNr = self.currentStep
        s.P = copy.deepcopy(self.currentPlayer)
        for i in range(self.nOfCorruption):
            s.wormSet.add(self.currentWormsSet[i])
        s.winer =    self.winer
        s.nofcorruption = self.nOfCorruption
        s.ECset = self.EC.playedCardsSet
        s.Wormset = self.WC.wormCardsSet 
        s.currentEC = copy.deepcopy(self.currentEC)
        s.ECset = self.EC.playedCardsSet
        self.listofSteps.append(s)
        return s

    def printgame(self,s):
        print("it is a game print in " +s)
        print("current player is")
        print(self.currentPlayer.Name)
        print("list of players")
        for i in range(self.nofPlayers):
            print(str(i)+":")
            print(self.listofPlayers[i].Name)
        for i in range(self.nofPlayers):
            print(str(i)+ ": ")
            self.listofPlayers[i].printMainRAM()
            