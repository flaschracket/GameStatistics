from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *
from enum import Enum



class Player():
    """description of class"""
    Name = ' '
#    PlayerResourceCards = Enum('PlayerResourceCards','')
    
    PlayerVars = MainRAMVars()
    GS = GameSettings()
    PlayerPC = [GS.GameHardware.CPU1, GS.GameHardware.MainRAM]

    PlayerReservedEC = []
    
    # decision parameters: parameters for making dicision
    #dp = []
    PCStatus = []
    counter = 0
    mydesicion = False
                

    def _init_(self):
        self.Name ='player1' 
        self.PlayerVars= self.PlayerVars._init_()
        return self
    def printstatus(self):
        print('The status of player is:')
        #print('PlayerName : '+self.Name)        
        #print('List of Hardwares : ')
        #print(list(Player.PlayerPC))
        #print('The Variables-Values of Main RAM are:')
        self.PlayerVars.print()

    def printVarsValue(self):
        print('the variable values of '+self.Name + ' are : ')
        self.PlayerVars.print()

    def printMainRAM(self):
        print('the MainRAM-variable values of '+ self.Name + ' are : ')
        self.PlayerVars.printinline()

            