from GameObjects.Player import *
from GameObjects.GameSettings import *
from random import randrange
import copy

class decision(object):
#----------------------------
    """description of class"""
    def _init_(self,ply):
     #deepcopy is extremly slow
        GS = GameSettings()
        self.restart = GS.restart
        self.PV = ply.playerVars
        self.tempPCstatus = ply.PCStatus
        self.decision = ply.myDecision
        self.tempReservedEc = ply.playerReservedEC
        self.nofRoundPausing = ply.nofRoundPausing
        self.buy = 'No'
        return self
#-------------------------------

    def makeRandomDecision(self):
        a = randrange(1000) % 2
        if a == 0:
           return True
        return False

    def playerAllowedToPlay(self):
        if 'CPU1Captured'  in (self.tempPCstatus):
            FuncName = 'rule1'
            funcresult = getattr(self, FuncName)()
        else:
            self.decision = True        
        return self

    #rule 1= cpu is captured  
    def rule1(self): 
            if (self.restart in self.tempReservedEc):
                self.tempPCstatus.remove('CPU1Captured')
                self.tempReservedEc.remove(self.restart)
                self.decision = True
                self.nofRoundPausing = 0
            else: 
                if (self.nofRoundPausing == 0):
                    self.tempPCstatus.remove('CPU1Captured')
                    self.decision = True
                else:
                    self.decision = False      
                    self.nofRoundPausing = self.nofRoundPausing-1
            return self
    #player can buy function from freelancer?
    def rule2(self):
        GS = GameSettings()
        if GS.freelancer in self.tempReservedEc:
                return True
            #for decision it is not need to check the price. 
        return False
    #player can buy CPU?
    def rule3(self):
        GS = GameSettings()
        if GS.bazar in self.tempReservedEc:
            return True
        return False

    #rule 5 = player decide buy something at first step of its turn    
    def rule5(self):
        buy = False
        buyFunc= self.rule2()
        buyHardware = self.rule3()
        #do I want to buy ?
        buy = self.makeRandomDecision()

        if buyFunc and buyHardware and buy:
            funcorhardware = self.makeRandomDecision()
            if funcorhardware:
                self.buy='Func'
            else: 
                self.buy='Hardware'
            return self
        #do I want to buy ?
        #buy = self.makeRandomDecision()
        if (buy and buyFunc): 
            self.buy = 'Func'
        if (buy and buyHardware):
           self.buy = 'Hardware'

        return self