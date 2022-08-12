from GameObjects.GameSettings import *
from GameObjects.Player import *
class Bazar():
    def __init__(self):
        self.gs = GameSettings()
        #self.player = Player('')
        return
    ################
    def buyCPU(self, player):
        isbought = False
        #1 means cpu
        bazarCard = [self.gs.bazar]
        sumvars = 0
        sumvars = player.playerVars.calculatesumvars()
        if (1 not in player.playerHardware) and (bazarCard in player.playerReservedEC):   
            if (player.playerVars.varsValue[3] >= self.gs.CPU):
                player.playerVars.varsValue[3] = player.playerVars.varsValue[3] - self.gs.CPU
                isbought = True
            elif (sumvars >= 50):
                self.reducePriceFromVars(player)                
                isbought = True
        else:
            isbought = False
        if isbought:
            player.playerHardware = [1]
            player.playerReservedEC.remove(bazarCard)
        return player

    
    def reducePriceFromVars(self, player):
        #reduce from A

        temp = player.playerVars.varsValue[0] - self.gs.CPU
        if temp > 0 :
            player.playerVars.varsValue[0] = temp
            player.playerHardware.append(1)
            return player
        player.playerVars.varsValue[0] = 0
        if (temp == 0):
            player.playerHardware.append(1)
            return player
        temp = ((-1) * temp)
        #reduce from B
        temp = player.playerVars.varsValue[1] - temp
        if temp > 0 :
            player.playerVars.varsValue[1] = temp
            player.playerHardware.append(1)
            return player
        player.playerVars.varsValue[1] = 0
        if temp == 0:
            player.playerHardware.append(1)
            return player
        temp = ((-1) * temp)
        #reduce from C
        temp = player.playerVars.varsValue[2] - temp
        if temp > 0 :
            player.playerVars.varsValue[2] = temp
            player.playerHardware.append(1)
            return player
        player.playerVars.varsValue[2] = 0
        player.playerHardware.append(1)
        return player
