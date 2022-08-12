from enum import Enum
from DB.dbCards import *
from GameObjects.Cards import *

class GameSettings():
    def __init__(self):
        self.gsID = 0
        self.sampleQuantity = 10
        self.winGoal = 128
        self.NrOfP = 2
        self.maxRound = 40
        self.Testchangelog = "test freelancer: Bazar: buy CPU is added"
        #the Id in DB
        self.restart = 200
        self.freelancer = 201
        self.bazar = 202
        self.CPU = 50
        return

    def ifWined(self,total):
         wined= False
         if (total >= self.winGoal):
                wined = True
         return wined
