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

    def __init__(self,samplecounter,gamesettings):
        self.GS = copy.deepcopy(gamesettings)
        #game vars
        self.currentRound = 0
        self.currentStep = 0
        self.samplecounter = samplecounter
        self.winer = ''
        
        # steps
        self.thisStep = Step(self.currentStep)
        #self.previousStep = Step(self.currentStep-1)
        #players-----------------
        self.listofPlayers = []
        for x in range(self.GS.NrOfP):
           name = 'Player '+ str(x)
           self.listofPlayers.append(Player(name))
        # insert game in DB
        self.gameID = mssql.insertGame(self)
        
        return   
    #---------------------
    def initialStep(self,x):
     #  playingdeck = self.GS.currentECdeck
     #  wcdeck = self.GS.currentWCdeck
        self.thisStep = Step(p = self.listofPlayers[x], gamesettings = self.GS , 
                             currentStep = self.currentStep,currentRound = self.currentRound)
        return self
    #---------------------

    def playOneRound(self):    
        for x in range(self.GS.NrOfP):
            self.initialStep(x)
            d = desicion()._init_(self.thisStep)
            self.thisStep = copy.deepcopy(d.playerdesicion())  
            self.thisStep = copy.deepcopy((self.thisStep.playOneStep()))
            #the objects are not updated automatically,
            #update GS for new currentdeck
            self.GS.currentECdeck= self.thisStep.GS.currentECdeck
            self.GS.currentWCdeck = self.thisStep.GS.currentWCdeck
            self.winer = self.thisStep.winer
            self.Stepsnapshot(self.thisStep)
            self.currentStep = self.currentStep + 1
            self.listofPlayers[x] = copy.deepcopy(self.thisStep.P)
            if (self.winer != ''):
                break             
        return self

    def Stepsnapshot(self,s):
        s.winer = self.winer
        #self.previousStep = copy.deepcopy(s)
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