from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *
from GameObjects.desicion import *
from enum import Enum
import copy



class Player():
    """description of class"""                

    def __init__(self,name):
        self.Name = name 
        self.playerVars = MainRAMVars()
        self.PCStatus = []
        self.nofRoundPausing = 0
        self.playerReservedEC = []
        self.mydesicion = True
        self.playerFuncs = []
        return 
   
    def updatePlayer(self,var,pause,reservedEC,damage,playerFuncs):
        self.playerVars = copy.deepcopy(var)
        self.nofRoundPausing = pause
        if (len(reservedEC)>0):
            self.playerReservedEC = reservedEC
        if (len(damage) > 0) and (damage[0] not in self.PCStatus):
            self.PCStatus = self.PCStatus + damage
        
        self.playerFuncs = playerFuncs
        self.playerVars.sumvars = self.playerVars.calculatesumvars()
        return

    def update_afterdecision(self,plydecision):
        #plydecision = desicion()
        self.mydesicion = plydecision.desicion
        self.nofRoundPausing = plydecision.nofRoundPausing
        self.PCStatus = plydecision.tempPCstatus
        self.playerReservedEC = plydecision.tempReservedEc
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
        
            