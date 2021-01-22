from GameObjects.MainRAMVars import MainRAMVars
from GameObjects.DefinedEnums import *
from enum import Enum



class Player():
    """description of class"""
    Name = ' '
    PlayerResourceCards = Enum('PlayerResourceCards','')
    PlayerPC = Enum('PlayerPC','MainRAM CPU1')
    PlayerVars = MainRAMVars()


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
        #self.PlayerVars.print()

    def printVarsValue(self):
        print('the variable values of '+self.Name + ' are : ')
        #self.PlayerVars.print()

    def printMainRAM(self):
        print('the MainRAM-variable values of '+ self.Name + ' are : ')
        self.PlayerVars.printinline()