
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *
from GameObjects.Cards import *

#import GameObjects.Cards import *

from copy import deepcopy
import mssql

# initial gamesettings
GS = GameSettings()

#tempply = Player('')
sampleCounter = 0

#previousStep = Step()

#connect to DB
#atabase.connectdb()

print("Hello From Game Simulation! Data Generation is begining")
GS.gsID = mssql.insertGameSettings(GS)
firstdeck = GS.currentECdeck
#GS.printall()
while sampleCounter <= GS.sampleQuantity:
    mygame = Game(sampleCounter,GS)
    firstdeck = GS.currentECdeck    
#    firstdeck = mygame.thisStep.EC.playingdeck
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
#mssql.update_GameSettings(firstdeck, GS.gsID)