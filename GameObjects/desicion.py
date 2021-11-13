from GameObjects.Player import *
from GameObjects.GameSettings import *
from random import randrange
import copy

class desicion(object):
    gs = GameSettings()

#----------------------------
    """description of class"""
    def _init_(self,s):
        self.step = copy.deepcopy(s)
        self.player = copy.deepcopy(s.P)
        return self
#-------------------------------

    def makeRandomDecision(self):
        a = randrange(1000) % 2
        if a == 0:
           return True
        return False
    def makeDecision(self):
            if self.GS.makeRandomDecision(): 
                if (self.GS.ResourceECTypes.Restart in (self.step.PlayerReservedEC)):
            
                  self.step.P.PlayerReservedEC.remove(self.DE.ResourceECTypes.Restart)
    def playerdesicion(self):

        if 'CPU1Captured'  in (self.player.PCStatus):
            FuncName = 'rule1'
            funcresult = getattr(self, FuncName)()
        else:
            self.step.playerDesicion = True        
        return self.step
    #rule 1= cpu is captured  
    def rule1(self): 
            if (self.gs.restart in self.player.PlayerReservedEC):
                self.step.P.PCStatus.remove('CPU1Captured')
                self.step.P.PlayerReservedEC.remove(self.gs.restart)
                self.step.playerDesicion = True
                self.step.P.nofRoundPausing = 0
            else: 
                if (self.player.nofRoundPausing == 0):
                    self.player.PCStatus.remove('CPU1Captured')
                    self.player.nofRoundPausing = 0
                    self.player.playerDesicion = True
                else:
                    self.step.playerDesicion = False      
                    self.player.nofRoundPausing = self.player.nofRoundPausing-1
            return self.step
