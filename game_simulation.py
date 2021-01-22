import module1
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *

mygame = Game()
tempply = Player()
#initial
print("Hello From Game Simulation! Data Generation is begining:")
mygame.nofPlayers = int(input("how many players are playing the game?"))
for x in range(mygame.nofPlayers):
    tempply.Name = "player"+str(x)
    mygame.listofPlayers.append(tempply) 

#play
condition = True

while condition:
    print(str(mygame.nofPlayers))
    mygame.currentRound = mygame.currentRound + 1
    mygame.playOneRound()   
    mygame.playOneRound()   
#    print("main round "+str(module1.mygame.currentRound))
    print(str(mygame.nofPlayers)) 
    if (mygame.winer != ''): 
        condition = False
print('*****Congradulation*****')
print(mygame.winer +' is the winer!')



