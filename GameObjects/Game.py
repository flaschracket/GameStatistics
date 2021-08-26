from GameObjects.GameSettings import *
from GameObjects.Step import *
from GameObjects.MainRAMVars import *
from GameObjects.Player import *
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from GameObjects.desicion import *
from random import randrange
import copy
import csv
from csv import writer
import mssql

class Game():
    """description of class"""

    def __init__(self,sc,s):
        self.listofPlayers = []
        self.thisStep = Step(sc)
        self.previousStep = copy.deepcopy(s)
        self.currentRound = 0
        self.currentStep = 0
        self.samplecounter = sc
        self.GS = GameSettings()
        for x in range(self.GS.NrOfP):
           name = 'Player '+ str(x)
           self.listofPlayers.append(Player(name))
           #print(self.listofPlayers[x])
        self.winer = ''
        self.currentWormsSet = []
        self.gameID = 0
        self.gameSettingsID = 0
        
        return   
    #---------------------
    def initialStep(self,x):
        resEC = self.previousStep.EC.reservedEC
        playingdeck = self.previousStep.EC.playingdeck
        wcdeck = self.previousStep.WC.playingdeck
#        nofrounds = self.previousStep.P.nofRoundPausing
        self.thisStep = Step(p = self.listofPlayers[x], reservedEC = resEC, 
                             currentStep = self.currentStep,currentRound = self.currentRound, 
                             samplecounter = self.samplecounter, playingdeck = playingdeck,wcdeck = wcdeck,nofpr = 0)
        return self
    #---------------------

    def playOneRound(self):    
        
        for x in range(self.GS.NrOfP):
            self.initialStep(x)
            d = desicion()._init_(self.thisStep)
            self.thisStep = copy.deepcopy(d.playerdesicion())  
           # self.printgame("after copy this step")
            #play one Step
            self.thisStep.playOneStep()
           # self.printgame("after play step")
            self.winer = self.thisStep.winer
            self.Stepsnapshot(self.thisStep)
            self.currentStep = self.currentStep + 1
            self.listofPlayers[x] = copy.deepcopy(self.thisStep.P)
            if (self.winer != ''):
                break             
        return self

    def Stepsnapshot(self,s):
        s.winer = self.winer
        self.previousStep = copy.deepcopy(s)
        mssql.insertStep(s,self.gameID,self.samplecounter)
        return self

    def printgame(self,s):
        
        print("it is a game print in " +s)
        print("step:" + str(self.currentStep))
        print("player: "+ self.thisStep.P.Name)
        print(self.thisStep.EC.nOfWC)
        print("playedwc")
        print(self.thisStep.WC.playedwc)    
        print("playedwcname")
        print(self.thisStep.WC.playedWCName)    
        print("played EC")
        print(self.thisStep.EC.ECName)
        print(" RAM ")
        self.thisStep.P.printMainRAM()
        print("-----------------------------")