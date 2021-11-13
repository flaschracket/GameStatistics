from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *
from enum import Enum
import copy



class Player():
    """description of class"""
   # GS = GameSettings()
   # PlayerPC = [GS.GameHardware.CPU1, GS.GameHardware.MainRAM]    
    
#    roundCounter = 0
    
                

    def __init__(self,name):
        self.Name = name 
        self.playerVars = MainRAMVars()
        self.PCStatus = []
        self.nofRoundPausing = 0
        self.PlayerReservedEC = []
        return 
   
    def updatePlayer(self,var,pause,reservedEC,damage):
        self.playerVars = copy.deepcopy(var)
        self.nofRoundPausing = pause
        if (len(reservedEC)>0):
            self.PlayerReservedEC = self.PlayerReservedEC + reservedEC
        if (len(damage) > 0) and (damage[0] not in self.PCStatus):
            self.PCStatus = self.PCStatus + damage

        return
        
    #----------------------
    #----------------------
    def printstatus(self):
        print('The status of player is:')
        self.playerVars.print()

    def printVarsValue(self):
        print('the variable values of '+self.Name + ' are : ')
        self.playerVars.print()

    def printMainRAM(self):
        print('the MainRAM-variable values of '+ self.Name + ' are : ')
        self.playerVars.printinline()
        
            