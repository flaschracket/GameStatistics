
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *
from copy import deepcopy
import mssql


tempply = Player('')
GS = GameSettings()
sampleCounter = 0


#initial

print("Hello From Game Simulation! Data Generation is begining:")
GS.NrOfP = int(input("how many players are playing the game?"))

while sampleCounter <= GS.sampleDataNumber:
    mygame = Game(sampleCounter)
    mssql.insertGame(mygame)
    for x in range(GS.NrOfP):
        name = 'Player '+ str(x)
        mygame.listofPlayers.append(Player(name))

    #play
    print("Game"+str(sampleCounter)+" begins")
    condition = True
    while condition:
        mygame.currentRound = mygame.currentRound + 1
        mygame = copy.deepcopy(mygame.playOneRound())          
        if (mygame.winer != '') or (mygame.currentRound >= GS.StoponThisRound): 
            condition = False
   
    mssql.updateGame(mygame)
    print("lenp = " + str(len(mygame.listofSteps)))
#    print("total = "+ (mygame.listofPlayers[mygame.currentRound-1].Name))
   # print('*****Congradulation*****')
    print(mygame.winer +' is the winer!')
    sampleCounter = sampleCounter +1


