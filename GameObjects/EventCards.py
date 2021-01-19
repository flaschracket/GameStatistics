from enum import Enum
from GameObjects.Player import *
class EventCards():
    """description of class"""
    totalEventCards = 10
    #EventCardType = Enum('EventCardType','ResourceEC WormEC TaskEC InputEC')

    def ECFunc0(self, p = Player()):
        p.PlayerVars.VarA = 5 
        mypenalty = 1
        return(mypenalty)

    def ECFunc1(self, p = Player()):
        p.PlayerVars.VarB = 10
        mypenalty = 2
        return(mypenalty)
    
    def ECFunc2(self, p= Player()):
        p.PlayerVars.VarC = 2  
        mypenalty = 3
        return(mypenalty)
    
    def ECFunc3(self, p= Player()):
        PV = p.PlayerVars
        PV.Total = PV.Total + PV.VarA + PV.VarB
        mypenalty = 1
        return(mypenalty)

    def ECFunc4(self, p= Player()):
        PV = p.PlayerVars
        PV.Total = PV.Total + PV.VarC + PV.VarB
        mypenalty = 1
        return(mypenalty)
    
    def ECFunc5(self, p= Player()):
        PV = p.PlayerVars
        PV.Total = PV.Total + PV.VarA+ PV.VarB + PV.VarC
        mypenalty = 1
        return(mypenalty)
    
    def ECFunc6(self):
        mypenalty = 1
        return(mypenalty)
    
    def ECFunc7(self):
        mypenalty = 0
        return(mypenalty)
    
    def ECFunc8(self):
        mypenalty = 1
        return(mypenalty)
    
    def ECFunc9(self):
        mypenalty = 0
        return(mypenalty)

    def ECFunc10(self):
        mypenalty = 1
        return(mypenalty)

    def ECFunc11(self):
        mypenalty = 0
        return(mypenalty)

