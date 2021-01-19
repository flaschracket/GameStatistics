from enum import Enum
from GameObjects.Player import *
class EventCards():
    """description of class"""
    totalEventCards = 10
    EventCardType = Enum('EventCardType','ResourceEC WormEC TaskEC InputEC')

    def ECFunc0(self, p = Player()):
        p.PlayerVars.VarA = 5 
        mystr = 'f0:'
        return(mystr)

    def ECFunc1(self, p = Player()):
        p.PlayerVars.VarB = 10
        mystr = 'f1:'
        return(mystr)
    def ECFunc2(self, p= Player()):
        p.PlayerVars.VarC = 2  
        mystr = 'f2:'
        return(mystr)
    def ECFunc3(self, p= Player()):
        PV = p.PlayerVars
        PV.Total = PV.Total + PV.VarA + PV.VarB
        mystr = 'f3:'
        return(mystr)
    def ECFunc4(self, p= Player()):
        PV = p.PlayerVars
        PV.Total = PV.Total + PV.VarC + PV.VarB
        mystr = 'f4:'
        return(mystr)
    def ECFunc5(self, p= Player()):
        PV = p.PlayerVars
        PV.Total = PV.Total + PV.VarA+ PV.VarB + PV.VarC
        mystr = 'f5:'
        return(mystr)
    def ECFunc6(self):
        mystr = 'f6:'
        return(mystr)
    def ECFunc7(self):
        mystr = 'f7:'
        return(mystr)
    def ECFunc8(self):
        mystr = 'f8'
        return(mystr)
    def ECFunc9(self):
        mystr = 'f9:'
        return(mystr)
    def ECFunc10(self):
        mystr = 'f10:'
        return(mystr)

    def ECFunc11(self):
        mystr = 'f10:'
        return(mystr)

