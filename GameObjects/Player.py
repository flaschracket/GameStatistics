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
        self.Name = 'MiniBit'
        Name = 'Asghar'

    def printstatus(self):
        print('The status of player is:')
        #print('1.List of Hardwares:')
        #print(list(Player.PlayerPC))
        print('2.The Variables-Values of Main RAM are:')
        self.PlayerVars.print()