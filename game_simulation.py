
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *
from copy import deepcopy
mygame = Game()
tempply = Player('')
GS = GameSettings()

#initial

print("Hello From Game Simulation! Data Generation is begining:")
GS.NrOfP = int(input("how many players are playing the game?"))

for x in range(GS.NrOfP):
    name = 'Player '+ str(x)
    mygame.listofPlayers.append(Player(name))

#play
print("Game begins")
condition = True
mygame.printgame("game_simulation")

while condition:
    mygame.currentRound = mygame.currentRound + 1
    mygame = copy.deepcopy(mygame.playOneRound())          
    if (mygame.winer != ''): 
        condition = False
print('*****Congradulation*****')
print(mygame.winer +' is the winer!')



