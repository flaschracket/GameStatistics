
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *
from copy import deepcopy
mygame = Game()
testgame = Game()
tempply = Player()
#initial
print("Hello From Game Simulation! Data Generation is begining:")
mygame.nofPlayers = int(input("how many players are playing the game?"))
for x in range(mygame.nofPlayers):
    mygame.listofPlayers.append(Player())
    mygame.listofPlayers[x].Name = "player" + str(x)
    #print("x"+str(x))
    #print(tempply.Name)
    #mygame.listofPlayers.append((copy.copy(tempply)))
    #mygame.listofPlayers.append(tempply)
    

#play
condition = True
mygame.printgame("game simulation")
#mygame.printgame("game_simulation")
while condition:
    #print(str(mygame.nofPlayers))
    
    mygame.currentRound = mygame.currentRound + 1
    mygame.playOneRound()   
    #print("t in main:"+str(mygame.currentPlayer.PlayerVars.Total))
#    print("main round "+str(module1.mygame.currentRound))
    #print(str(mygame.nofPlayers)) 
    if (mygame.winer != ''): 
        condition = False
print('*****Congradulation*****')
print(mygame.winer +' is the winer!')



