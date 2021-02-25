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
   #     if 'CPU1Captured'  in (self.step.P.PCStatus):
   #           FuncName = 'rule1'
    #          funcresult = getattr(self, FuncName)()
    #    else:
        self.step.playerDesicion = True        
        return self.step
#rule 1= cpu is captured  
    def rule1(self): 
            if (self.gs.ResourceECTypes.Restart in self.step.P.PlayerReservedEC):
                self.step.P.PCStatus.remove('CPU1Captured')
                self.step.P.PlayerReservedEC.extend('Restart')
                self.step.playerDesicion = True
                self.step.P.counter = 0
            else: 
                if (self.step.P.counter == self.gs.pauseplayingcount):
                    self.step.P.PCStatus.remove('CPU1Captured')
                    self.step.P.counter = 0
                    self.step.playerDesicion = True
                else:
                    self.step.playerDesicion = False      
                    self.step.P.counter = self.step.P.counter+1
            return self.step
