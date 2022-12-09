
from random import randrange
from pyGameSimulator.GameObjects.Player import *
from GameObjects.Game import *
from GameObjects.Cards import *
from DB.dbGameSettings import *
from copy import deepcopy

import mssql

# initial gamesettings

GS = GameSettings()
GD = GameDeck()
sampleCounter = 0
dbgs = dbGameSettings()
print("Hello From Game Simulation! Data Generation is begining")
gsID = dbgs.insert_GameSettings(GD)

while sampleCounter <= GS.sampleQuantity:
# it should have if the deck is devided else mixed
#    GD.currentECdeck = GD.initialEC.shuffle()
#    GD.currentWCdeck = GD.initialWC.shuffle()
    GD.currentMixedCards = GD.initialMixedCards.shuffle()
    mygame = Game(sampleCounter,GD,gsID)
    #play
    print("---Game : "+str(sampleCounter)+"---")
    condition = True
    
    while condition:        
        mygame.currentRound = mygame.currentRound + 1
        #mygame = copy.deepcopy(mygame.playOneRound())
        mygame.playOneRound() 
        if (mygame.winer != '') or (mygame.currentRound >= GS.maxRound): 
            condition = False              
    mssql.updateGame(mygame)
    print('winner :'+mygame.winer )
    print('------------------------------')
    sampleCounter = sampleCounter +1
