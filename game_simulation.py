
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *
from GameObjects.Cards import *
from copy import deepcopy
import mssql

# initial gamesettings
GS = GameSettings()

sampleCounter = 0

print("Hello From Game Simulation! Data Generation is begining")
GS.gsID = mssql.insertGameSettings(GS)

while sampleCounter <= GS.sampleQuantity:
    mygame = Game(sampleCounter,GS)
    #play
    print("---Game : "+str(sampleCounter)+"---")
    condition = True
    
    while condition:        
        mygame.currentRound = mygame.currentRound + 1
        mygame = copy.deepcopy(mygame.playOneRound()) 
        if (mygame.winer != '') or (mygame.currentRound >= GS.maxRound): 
            condition = False              
    mssql.updateGame(mygame)
    print('winner : ' +mygame.winer )
    print('------------------------------')
    sampleCounter = sampleCounter +1
