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
    const = GameSettings()
    winer = ''
    nofPlayers = 0
    currentRound = 0
    currentEC = 0
    currentWC = 0
    currentWormsSet = {}
    currentStep = 0
    #currentPenalty = 0
    currentPlayer = Player()
    listofPlayers = []
    listofSteps = []
    EC = EventCards()
    WC = WormCards()
    DE = GameSettings()
    

    

    def ifWined(self):
        wined= False
        if (self.currentPlayer.PlayerVars.Total > self.DE.winGoal):
            wined = True
            self.winer = self.currentPlayer.Name
        return (self)
    
    def playEC(self):
        """calling a function with making its name as string"""
        self.currentEC = self.EC.SelectNextEC()
        self.EC.PV = copy.deepcopy(self.currentPlayer.PlayerVars)
        FuncName = 'ECFunc' + str(self.currentEC)
        getattr(self.EC, FuncName)()
        self.currentPlayer.PlayerVars = copy.deepcopy(self.EC.PV)
        #self.printgame("PlayEC")
        return(self)

    def playWC(self):
        self.WC.SelectNextWC()
        self.WC.PV = copy.deepcopy(self.currentPlayer.PlayerVars)
        FuncName = 'WCFunc' + str(self.WC.currentWC)
        funcresult = getattr(self.WC, FuncName)()
        self.currentPlayer.PlayerVars = copy.deepcopy(self.WC.PV)
        #OMGCorruption(self,myturn)
        return (self)

    def playOneStep(self):
        self.playEC()
        self.ifWined()
        #self.EC.playedCardsSet.add(self.currentEC)
        if (self.winer != ''):
            self.Stepsnapshot()
            #s = copy.deepcopy(self.Stepsnapshot())    
            return (self)
        for i in range(self.EC.nOfWC):
            self.playWC()
        self.Stepsnapshot()
        self.listofSteps[self.currentStep].printCSV()
        #self.printgame("step")
        self.currentStep = self.currentStep+1
        return (self)
    
    def playOneRound(self):
        for x in range(self.nofPlayers):
            self.currentPlayer = copy.deepcopy(self.listofPlayers[x])
            #self.printgame("round1:")
            self.playOneStep()
            #self.printgame("round2:")
            self.listofPlayers[x] = copy.deepcopy(self.currentPlayer)
            if (self.winer != ''):
                break            
            self.currentEC = self.EC.currentEC
        return self

    def Stepsnapshot(self):
        s = Step()
        s.roundNr = self.currentRound
        s.stepNr = self.currentStep
        s.P = copy.deepcopy(self.currentPlayer)
        
        #for i in range(self.const.NrOfWC):
        #s.wormSet.add((self.currentWormsSet))
        s.winer = self.winer
#        s.nofcorruption = self.nOfCorruption
        s.playedECset = self.EC.playedCardsSet
#        s.Wormset = self.WC.playedWormCardsSet 
        s.currentEC = copy.deepcopy(self.currentEC)
        s.playedWormsSet = self.WC.playedWormCardsSet
        s.nOfWC = self.EC.nOfWC
        self.listofSteps.append(s)
        #self.printgame("stepsnapshot")
        return s

    def printgame(self,s):
        print("it is a game print in " +s)
        print("step nr:"+str(self.currentStep))
        print("nr of WCs:"+str(self.EC.nOfWC))
        #print("nr of WCs:"+str(self.nOfWC))
        #print("current player is:", end =" ")
        #print(self.currentPlayer.Name)
        #print("list of players")
        #for i in range(self.nofPlayers):
         #   print(str(i)+":", end =" ")
          #  print(self.listofPlayers[i].Name)
        #for i in range(self.nofPlayers):
            #print(str(i)+ ": ", end="")
            #self.listofPlayers[i].printMainRAM()
        #print("current winer is:"+self.winer)
        print("playedWC: "+str(self.WC.playedWormCardsSet)+",", end= " ")   
        print("Current WC:" + str(self.currentWC))