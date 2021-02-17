from GameObjects.Game import *
from GameObjects.Player import *
import csv
from csv import writer



class Step():
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
    winer = ''
    nOfWC = 0
    currentEC = 0
    roundNr = 0
    stepNr = 0
    P = Player()
    playedECset = {}
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
    
    def printCSVHeader(self):
        print("roundnr,stepnr,player,A,B,C,Total,winer,ec,ecset,nofworms,wcs,wormset;")
        return (True)
    
    def printCSV(self):
        self.printCSVHeader()
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
        print(str(self.nOfWC)+",",end=" ")
        print(str(self.playedWormsSet),end="")
        print(";")
        
    def setAllValuesinLine(self):
       #fnames = [ 'stepnr', 'player'] 
                 #,'A', 'B', 'C', 'Total', 'winer', 'ec', 'ecset', 'nofworms', 'wcs', 'wormset']
       allvalues = "{'roundnr':,"+str(self.roundNr)+"'player':,"+str(self.roundNr)+"}"
       #+"," + str(self.stepNr) +"," + self.P.Name+"," + str(self.P.PlayerVars.VarA)+"," + str(self.P.PlayerVars.VarB)+"," + str(self.P.PlayerVars.VarC)+","+str(self.P.PlayerVars.Total)+"," + self.winer+","+str(self.currentEC)+","+ str(self.playedECset)+","+ str(self.nOfWC)+","+str(self.playedWormsSet)+";"
       return(allvalues)

    def addlinetoCSVF(self):
        PV = (self.P.PlayerVars)
        rowlist = [self.roundNr,self.stepNr,self.P.Name, PV.VarA, PV.VarB, PV.VarC, PV.Total, self.winer, self.currentEC,self.playedECset,self.nOfWC,self.playedWormsSet]
        with open('gameData2.csv', 'a+', newline='') as f:
            csvwriter = writer(f,delimiter=';')
            csvwriter.writerow(rowlist)        
        f.close()
        return True