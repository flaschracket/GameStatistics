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
        self.thisStep = Step(p = self.listofPlayers[x], reservedEC = resEC, 
                             currentStep = self.currentStep,currentRound = self.currentRound, 
                             samplecounter = self.samplecounter, playingdeck = playingdeck,wcdeck = wcdeck)
        return self
    #---------------------

    def playOneRound(self):    
        
        for x in range(self.GS.NrOfP):
            self.initialStep(x)
            d = desicion()._init_(self.thisStep)
            self.thisStep = copy.deepcopy(d.playerdesicion())  
            #play one Step
            print("----round----")
            print(self.currentRound)
            self.thisStep.playOneStep()
            self.winer = self.thisStep.winer
            self.Stepsnapshot(self.thisStep)
            self.currentStep = self.currentStep+1
            self.listofPlayers[x] = copy.deepcopy(self.thisStep.P)
            if (self.winer != ''):
                break            
            print("--nextplayer----")
        print("xxx") 
        return self

    def Stepsnapshot(self,s):
        s.winer = self.winer
        self.previousStep = copy.deepcopy(s)
        mssql.insertStep(s,self.gameID,self.samplecounter)
        return self

    def printgame(self,s):
        print("it is a game print in " +s)
        for i in range(self.GS.NrOfP):
            print(str(i)+ ": ", end="")
            self.listofPlayers[i].printMainRAM()
        print("end")