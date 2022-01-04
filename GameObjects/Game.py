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

    def __init__(self,samplecounter,currentgamedeck,gsID):
        self.GD = currentgamedeck
        self.GS = GameSettings()
        # make the cards list a new random combination
        #self.GS.
        #game vars
        self.currentRound = 0
        self.currentStep = 0
        self.samplecounter = samplecounter
        self.winer = ''
        # steps
        self.thisStep = Step(currentStep = self.currentStep, currentgamedeck = self.GD)
        #self.previousStep = Step(self.currentStep-1)
        #players-----------------
        self.listofPlayers = []
        for x in range(self.GS.NrOfP):
           name = 'Player '+ str(x)
           self.listofPlayers.append(Player(name))
        # insert game in DB
        self.gamesettingsID = gsID
        self.gameID = mssql.insertGame(self)        
        return   
    #---------------------
    def initialStep(self,x):
     #  playingdeck = self.GS.currentECdeck
     #  wcdeck = self.GS.currentWCdeck
        self.thisStep = Step(p = self.listofPlayers[x], currentStep = self.currentStep, 
                             currentRound = self.currentRound, currentgamedeck = self.GD)
        return self
    #---------------------

    def playOneRound(self):    
        for x in range(self.GS.NrOfP):
            self.initialStep(x)
            self.thisStep.playOneStep()
            #Step_updateafterplayone
            #self.thisStep = copy.deepcopy((self.thisStep.playOneStep()))
            #the objects are not updated automatically,
            #update GS for new currentdeck
            #self.GD.currentECdeck= self.thisStep.EC.playingdeck
            #self.GD.currentWCdeck = self.thisStep.WC.playingdeck
            self.GD.currentMixedCards = self.thisStep.currentMixedCards
            self.winer = self.thisStep.winer
            self.Stepsnapshot(self.thisStep)
            self.currentStep = self.currentStep + 1
            #self.listofPlayers[x] = copy.deepcopy(self.thisStep.P)
            #update player
            self.listofPlayers[x].playerVars = self.thisStep.P.playerVars
            self.listofPlayers[x].PCStatus = self.thisStep.P.PCStatus
            self.listofPlayers[x].mydesicion = self.thisStep.P.mydesicion
            self.listofPlayers[x].PlayerReservedEC = self.thisStep.P.PlayerReservedEC
            #self.update()
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