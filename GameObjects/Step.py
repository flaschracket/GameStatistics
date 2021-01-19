from GameObjects.Game import *
from GameObjects.Player import *


class Step():
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
    G = Game()
    p = Player()
    currentStep = 0
    def _init_(self,g = Game(),p = Player()):
        self.currentStep = 1

    def stepstatus(self):
        stepHeaderInfo = "Step : " + str(currentStep) + str(self.G.CurrentRound) + " Player : " + self.P.Name 
        print(stepHeaderInfo)

