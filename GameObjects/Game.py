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
        return   
    #---------------------
    def initialStep(self,x):
        pec = self.previousStep.EC.playedEC
        resEC = self.previousStep.EC.reservedEC
        pwc = self.previousStep.WC.playedWC
        rec = self.previousStep.EC.resourceEC                
        self.thisStep = Step(p = self.listofPlayers[x], playedWC = pwc,playedEC = pec, reservedEC = resEC,resourceEC = rec, currentStep = self.currentStep,currentRound = self.currentRound, samplecounter = self.samplecounter)
        return self
    #---------------------

    def playOneRound(self):    
        
        for x in range(self.GS.NrOfP):
            self.listofPlayers[x].Ec
            self.initialStep(x)
            d = desicion()._init_(self.thisStep)
            self.thisStep = copy.deepcopy(d.playerdesicion())  
            #play one Step
            self.thisStep.playOneStep()
            self.winer = self.thisStep.winer
            self.Stepsnapshot(self.thisStep)
            self.currentStep = self.currentStep+1
            self.listofPlayers[x] = copy.deepcopy(self.thisStep.P)
            if (self.winer != ''):
                break            
        return self

    def Stepsnapshot(self,s):
        s.winer = self.winer
        self.previousStep = copy.deepcopy(s)
        mssql.insertStep(s,self.samplecounter)
        return self

    def printgame(self,s):
        print("it is a game print in " +s)
        for i in range(self.GS.NrOfP):
            print(str(i)+ ": ", end="")
            self.listofPlayers[i].printMainRAM()
        print("end")