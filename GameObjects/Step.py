from GameObjects.Game import *
from GameObjects.Player import *

class Step():
    
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
    roundNr = 0
    StepNr = 0
    P = Player()
    ECset = {}
    Wormset = {}

    def _init_():
        self.roundNr = 0

    def stepstatus(self):
        stepHeaderInfo =  "Round number: " +str(self.roundNr)+" Step : " + str(self.currentStep)+" Player of this step: "  + self.P.Name 
        print(stepHeaderInfo)
        self.P.printMainRAM()