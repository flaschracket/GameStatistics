from GameObjects.Game import *
from GameObjects.Player import *
import csv
from csv import writer



class Step():
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
    winer = ''
    nOfWC = 0
    roundNr = 0
    stepNr = 0
    currentEC = 0
    PlayedECName = ''
    P = Player()
    playedECset = {}
    playedWormsSet = {}
    playedWCName = {}

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
    
    def printCSVHeader(self):
        print("roundnr,stepnr,player,A,B,C,Total,winer,ec,ecset,nofworms,wcs,wormset;")
        return (True)
    
 

    def addlinetoCSVF(self):
        PV = (self.P.PlayerVars)
        rowlist = [self.roundNr,self.stepNr,self.P.Name, PV.VarsValue[0], PV.VarsValue[1], PV.VarsValue[2]]
        rowlist = rowlist + [PV.VarsValue[3],PV.Nullindex , self.currentEC,self.playedECset,self.nOfWC]
        rowlist = rowlist+ [self.playedWormsSet,self.P.mydesicion ,self.P.PCStatus, self.P.counter]
        rowlist = rowlist + [self.PlayedECName, self.PlayedWCName,self.winer]
        with open('gameData2.csv', 'a+', newline='') as f:
            csvwriter = writer(f,delimiter=';')
            csvwriter.writerow(rowlist)        
        f.close()
        return True