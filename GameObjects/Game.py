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
    GS = GameSettings()

    winer = ''
    currentWormsSet = []
    
    #currentPenalty = 0
    listofPlayers = []
    listofSteps = []
    
    
    def __init__(self,sc):
        self.currentRound = 0
        self.currentStep = 0
        self.samplecounter = sc
        return   
    #---------------------
    #---------------------
    
    def playOneRound(self):
        ecp = set() 
        ecr = set()
        pwc = set()
        rec = set()
        for x in range(self.GS.NrOfP):
            if (len(self.listofSteps)>0):
                ecp = self.listofSteps[self.currentStep-1].EC.playedEC
                ecr = self.listofSteps[self.currentStep-1].EC.reservedEC
                pwc = self.listofSteps[self.currentStep-1].WC.playedWC
                rec = self.listofPlayers[x].PlayerReservedEC
                self.listofSteps[self.currentStep-1].EC.resourceEC
            newStep = Step(self.listofPlayers[x],ecp,ecr,pwc,rec,self)
            d = desicion()._init_(newStep)
            newStep = copy.deepcopy(d.playerdesicion())            
            #play one STep
            newStep.playOneStep()
            self.winer = newStep.winer
            self.Stepsnapshot(newStep)
            self.currentStep = self.currentStep+1
            self.listofPlayers[x] = copy.deepcopy(newStep.P)
            if (self.winer != ''):
                break            
        return self

    def Stepsnapshot(self,s):
        s.winer = self.winer
        self.listofSteps.append(s)
        mssql.insertStep(s,self.samplecounter)
        return self

    def printgame(self,s):
        print("it is a game print in " +s)
        for i in range(self.GS.NrOfP):
            print(str(i)+ ": ", end="")
            self.listofPlayers[i].printMainRAM()
        print("end")