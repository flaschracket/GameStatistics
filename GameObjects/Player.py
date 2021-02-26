from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *
from enum import Enum
import copy



class Player():
    """description of class"""
    #Name = ' '

    #PlayerVars = MainRAMVars()
    GS = GameSettings()
    PlayerPC = [GS.GameHardware.CPU1, GS.GameHardware.MainRAM]

    PlayerReservedEC = []
    
    PCStatus = []
    roundCounter = 0
    
                

    def __init__(self,name):
        self.Name = name 
        self.playerVars = MainRAMVars()
        self.PCStatus = []
        return 
    def updatePlayer(self,var):
        self.playerVars = copy.deepcopy(var)    
    #----------------------
    #----------------------
    def printstatus(self):
        print('The status of player is:')
        #print('PlayerName : '+self.Name)        
        #print('List of Hardwares : ')
        #print(list(Player.PlayerPC))
        #print('The Variables-Values of Main RAM are:')
        self.playerVars.print()

    def printVarsValue(self):
        print('the variable values of '+self.Name + ' are : ')
        self.playerVars.print()

    def printMainRAM(self):
        print('the MainRAM-variable values of '+ self.Name + ' are : ')
        self.playerVars.printinline()
        
            