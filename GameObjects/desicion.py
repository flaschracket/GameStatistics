from GameObjects.Player import *
from GameObjects.GameSettings import *
from random import randrange
import copy

class desicion(object):
#    gs = GameSettings()

#----------------------------
    """description of class"""
    def _init_(self,ply,GS):
     #   self.step = copy.deepcopy(s)
        self.player = copy.deepcopy(ply)
        gs = copy.deepcopy(Gs)
    return self
#-------------------------------

    def makeRandomDecision(self):
        a = randrange(1000) % 2
        if a == 0:
           return True
        return False

#    def makeDecision(self):
 #           if self.GS.makeRandomDecision(): 
  #              if (self.GS.ResourceECTypes.Restart in (self.step.PlayerReservedEC)):
   #         
    #              self.step.P.PlayerReservedEC.remove(self.DE.ResourceECTypes.Restart)

    def playerdesicion(self):
        if 'CPU1Captured'  in (self.player.PCStatus):
            FuncName = 'rule1'
            funcresult = getattr(self, FuncName)()
        else:
            self.player.playerDesicion = True        
        return self
    #rule 1= cpu is captured  
    def rule1(self): 
            if (self.gs.restart in self.player.PlayerReservedEC):
                self.player.PCStatus.remove('CPU1Captured')
                self.player.PlayerReservedEC.remove(self.gs.restart)
                self.player.playerDesicion = True
                self.playerfRoundPausing = 0
            else: 
                if (self.player.nofRoundPausing == 0):
                    self.player.PCStatus.remove('CPU1Captured')
                    self.player.nofRoundPausing = 0
                    self.player.playerDesicion = True
                else:
                    self.player.playerDesicion = False      
                    self.player.nofRoundPausing = self.player.nofRoundPausing-1
            return self
