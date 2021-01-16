import module1
from GameObjects.Player import *

player1 = Player()

player1.Name = 'MiniBit1'

print("Hello From Game Simulation! Data Generation is begining:")
while True:
    module1.GoForward(module1)
    print(str(module1.CurrentStep))
    if (player1.PlayerVars.Total > 499): 
        print('You Won!')
        break
    print(player1.printstatus())


