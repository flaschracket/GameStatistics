from GameObjects.Game import *
from GameObjects.Player import *

class Step():
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
    winer = ''
    nofcorruption = 0
    currentEC = 0
    roundNr = 0
    stepNr = 0
    P = Player()
    playedECset = {}
    wormSet = {}
    #totalECset ={}
    playedWormsSet = {}

    def printStepStatus(self):
        print("----------------------------------------------")
        print("------------ Main Information: ---------------")
        stepHeaderInfo ="Round N.: "+str(self.roundNr)+" -Step N.: "+str(self.stepNr)+" Player: "+ self.P.Name+" Winer:"+self.winer 
        print(stepHeaderInfo)
        print("---------------- Event Cards -----------------")
        whatPlayed = "Event Card: " + str(self.currentEC)+" Nr. of worm Cards: " +str(self.nofcorruption)+" Played Worm Cards: " +str(self.Wormset) + " "
        print(whatPlayed)
        print("-------- Variable Values of Main RAM ---------")
        self.P.printMainRAM()
        print("-------- played EC set ---------")
        print("EC set: "+str(self.playedECsett))
        print("----------------------------------------------")

    def printCSV(self):
      #  print("roundnr,stepnr,player,A,B,C,Total,winer,ec,ecset,wcnr,wcs,wormset;")
        print(str(self.roundNr)+",",end=" ")
        print(str(self.stepNr) +",",end=" ")
        print(self.P.Name+",",end=" ")
        print(str(self.P.PlayerVars.VarA)+",",end=" ")
        print(str(self.P.PlayerVars.VarB)+",",end=" ")
        print(str(self.P.PlayerVars.VarC)+",",end=" ")
        print(str(self.P.PlayerVars.Total)+",",end=" ")
        print(self.winer+",",end=" ")
        print(str(self.currentEC)+",",end=" ")
        print(str(self.playedECset)+",",end=" ")

        print(str(self.nofcorruption)+",",end=" ")
        print(str(self.Wormset)+",",end=" ")
        
        
        print(str(self.playedWormsSet)+",",end=" ")
        



        print(";")
        