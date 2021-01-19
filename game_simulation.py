import module1
from GameObjects.Player import *

player1 = Player()

player1.Name = 'MiniBit1'

print("Hello From Game Simulation! Data Generation is begining:")
#set up players and game condition
module1.Gamesetup(module1)
condition = True
currentround = 1
while condition:
    module1.playARound(module1)
    currentround = currentround + 1 
    print('current round is' + str(currentround)) 
    if (module1.G.Winer != ''): 
        condition = False
print('*****Congradulation*****')
print(module1.G.Winer +' is the winer!')



