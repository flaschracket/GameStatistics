from GameObjects.Player import *
from GameObjects.GameSettings import *
from random import randrange
import copy

class desicion(object):
    p = Player()
    gs = GameSettings()

#----------------------------
    """description of class"""
    def _init_(self,p):
        self.p = copy.deepcopy(p)
        return self


#-------------------------------
    def makeRandomDecision(self):
        a = randrange(1000) % 2
        if a == 0:
           return True
        return False

    def makeDecision(self):
            if self.GS.makeRandomDecision(): 
                if (self.GS.ResourceECTypes.Restart in (self.currentPlayer.PlayerReservedEC)):
            
                  self.currentPlayer.PlayerReservedEC.remove(self.DE.ResourceECTypes.Restart)
    def playerdesicion(self):
        if 'CPU1Captured'  in (self.p.PCStatus):
              FuncName = 'rule1'
              funcresult = getattr(self, FuncName)()
        else:
            self.p.mydesicion = True        
        return self.p
#rule 1= cpu is captured  
    def rule1(self): 
            if (self.gs.ResourceECTypes.Restart in self.p.PlayerReservedEC):
                self.p.PCStatus.remove('CPU1Captured')
                self.p.PlayerReservedEC.extend('Restart')
                self.p.mydesicion = True
                self.p.counter = 0
            else: 
                if (self.p.counter == self.gs.pauseplayingcount):
                    self.p.PCStatus.remove('CPU1Captured')
                    self.p.counter = 0
                    self.p.mydesicion = True
                else:
                    self.p.mydesicion = False      
                    self.p.counter = self.p.counter+1
            return self.p
