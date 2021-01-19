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
    print('winer:' + module1.Winer)
    if (module1.Winer != ''): 
        condition = False
print('*****Congradulation*****')
print(module1.Winer +' is the winer!')



