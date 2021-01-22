from GameObjects.DefinedEnums import *
from GameObjects.Step import *
from GameObjects.MainRAMVars import *
from GameObjects.Player import *
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from random import randrange


class Game():
    """description of class"""
    winer = ''
    sumplayedEC = 0 
    nofPlayers = 0
    nOfCorruption = 0

    currentRound = 0
    currentEC = 0
    currentWorm = 0
    currentStep = 0
    currentPlayer = Player()
    
    
       
    listofPlayers = []
    listofSteps = []
    EC = EventCards()
    WC = WormCards()
    DE = DefinedEnums()


    

    def ifWined(self):
        wined= False
        if (self.currentPlayer.PlayerVars.Total > self.DE.winGoal):
            print("winer true:" + self.winer)
            wined = True
            self.winer = self.currentPlayer.Name
        print("winer:" + self.winer)
        return (self)
    
    def playEC(self):
        """calling a function with making its name as string"""
        self.currentEC = 1
        #self.currentEC = self.EC.SelectEC()
        #print("EC-a "+ str(self.currentEC))
        FuncName = 'ECFunc' + str(self.currentEC)
        funcresult_player = getattr(self.EC, FuncName)()
        return(funcresult_player)

    def playWC(self):
        self.currentWC = self.WC.selectWC()
        FuncName = 'WCFunc' + str(self.currentWC)
        funcresult = getattr(self.WC, FuncName)()
        #OMGCorruption(self,myturn)
        return True

    def playOneStep(self):
 #       print("step:"+str(self.currentStep))
        self.currentStep = self.currentStep+1
        self.currentPlayer = self.playEC()
        ####step corruption should be developed
#        print("step corruption:"+str(self.nOfCorruption))
        self.currentPlayer.printMainRAM()
        self.currentPlayer.PlayerVars.Total = 100
        #print("T:"+str(self.currentPlayer.PlayerVars.Total))

        if (self.ifWined() == True):
            self.Stepsnapshot()    
            return (self)
        for i in range(self.nOfCorruption):
            self.playWC()
        self.sumplayedEC = self.EC.Set(self.sumplayedEC)
        self.Stepsnapshot()
        return (self)
    
    def playOneRound(self):
        #print("round " +str(self.currentRound))
        #print("players of round"+str(self.nofPlayers))
        for x in range(self.nofPlayers):
            #print("x is " + str(x))
            self.currentPlayer = self.listofPlayers[x]
            self.sumPlayedEC = self.sumplayedEC + 1
            self.playOneStep()
            self.currentPlayer.printMainRAM()
            #print("t="+ str(self.currentPlayer.PlayerVars.Total))             
            #print("winer:"+self.winer)
            if (self.winer != ''):
                break            
        return self

    def Stepsnapshot(self):
        s = Step()
        s.CurrentStep = self.currentStep
        s.currentRound = self.currentRound
        s.P = self.currentPlayer
        s.ECset = self.EC.playedCardsSet
        s.Wormset = self.WC.wormCardsSet 
        s.currentEC = self.currentEC
        s.currentWorm = self.currentWorm
        self.listofSteps.append(s)

