from GameObjects.Game import *
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from GameObjects.Player import *
import copy
import csv
from csv import writer



class Step():
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
      

    def __init__(self,p,ecp,ecr,g):
        self.P  = copy.deepcopy(p)
        pv = copy.deepcopy(self.P.playerVars)
        self.playedEC = ecp
        self.reservedEC = ecr        
        self.EC = EventCards(pv,self.playedEC,self.reservedEC)
        self.WC = WormCards(pv)
        self.playerDesicion = False
        self.stepNr = g.currentStep
        self.roundNr = g.currentRound
        self.winer = ''
        self.GS = copy.deepcopy(g.GS)
        return

    def updatePlayer(self):
        self.P.playerVars = copy.deepcopy(self.WC.PV) 
        self.P.PCStatus = self.WC.damages
        return self
    #-------------------------
    #-------------------------
    def playWC(self):
        self.WC.playFunc(self)
        self.updatePlayer()
        return self
    
    def playOneStep(self):
        # if (self.playerDesicion):
        self.EC.playFunc(self)
       
        t = self.P.playerVars.varsValue[3]
#        if (self.GS.ifWined(t))
 #           self.winer = self.P.Name
  #          self.addlinetoCSVF()
   #         return (self)
        if (self.playerDesicion == True):
            for i in range(self.EC.nOfWC):
                self.WC.playFunc()
                self.P.updatePlayer(self.WC.PV)
        self.addlinetoCSVF()
        return (self)



    def printStepStatus(self):
        print("----------------------------------------------")
        print("------------ Main Information: ---------------")
       # stepHeaderInfo ="Round N.: "+str(self.roundNr)+" -Step N.: "+str(self.stepNr)+" Player: "+ self.P.Name+" Winer:"+self.winer 
        print(stepHeaderInfo)
        print("---------------- Event Cards -----------------")
        #whatPlayed = "Event Card: " + str(self.currentEC)+" Nr. of worm Cards: " +str(self.nofcorruption)+" Played Worm Cards: " +str(self.Wormset) + " "
        print(whatPlayed)
        print("-------- Variable Values of Main RAM ---------")
        self.P.printMainRAM()
        print("-------- played EC set ---------")
        #print("EC set: "+str(self.playedECsett))
        print("----------------------------------------------")
    
    def printCSVHeader(self):
        print("roundnr,stepnr,player,A,B,C,Total,winer,ec,ecset,nofworms,wcs,wormset;")
        return (True)
    
 

    def addlinetoCSVF(self):
        PV = (self.P.playerVars)
        rowlist = [self.roundNr,self.stepNr,self.P.Name, PV.varsValue[0], PV.varsValue[1], PV.varsValue[2]]
        rowlist = rowlist + [PV.varsValue[3],PV.Nullindex , self.EC.currentEC,self.EC.nOfWC]
        rowlist = rowlist+ [self.playerDesicion ,self.P.PCStatus, self.P.counter]
        rowlist = rowlist + [self.EC.ECName, self.WC.playedWCName,self.winer,self.EC.playedEC, self.WC.playedWC]
        with open('gameData2.csv', 'a+', newline='') as f:
            csvwriter = writer(f,delimiter=';')
            csvwriter.writerow(rowlist)        
        f.close()
        return True