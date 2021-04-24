
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *
from GameObjects.Cards import *
#import GameObjects.Cards import *

from copy import deepcopy
import mssql

tempply = Player('')
GS = GameSettings()
sampleCounter = 0

previousStep = Step()

#initial

print("Hello From Game Simulation! Data Generation is begining:")
gsID = mssql.insertGameSettings(GS)
while sampleCounter <= GS.sampleQuantity:
    mygame = Game(sampleCounter,previousStep)
    mygame.gameSettingsID = gsID
    mygame.gameID = mssql.insertGame(mygame)
    #play
    print("Game"+str(sampleCounter)+" begins")
    condition = True
    while condition:        
        mygame.currentRound = mygame.currentRound + 1
        mygame = copy.deepcopy(mygame.playOneRound()) 
        if (mygame.winer != '') or (mygame.currentRound >= GS.maxRound): 
            condition = False              
    mssql.updateGame(mygame)
    print(mygame.winer +' is the winer!')
    sampleCounter = sampleCounter +1
