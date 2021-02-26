from GameObjects.Game import *
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from GameObjects.Player import *
import copy
import csv
from csv import writer



class Step():
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
      

    def __init__(self,p,ecp,ecr,pwc,rec,g):      
        self.playedWC = pwc
        self.playedEC = ecp
        self.reservedEC = ecr

        self.P  = copy.deepcopy(p)
        pv = copy.deepcopy(self.P.playerVars)
        self.EC = EventCards(pv,ecp,ecr,rec)
        self.WC = WormCards(pv,pwc)
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
        total=0
        if self.playerDesicion:
            self.EC.playFunc(self)  
            
            total = self.P.playerVars.varsValue[3]
        if (self.GS.ifWined(total)):
             self.winer = self.P.Name
             self.addlinetoCSVF()
             return (self)
        if (self.playerDesicion):
            for i in range(self.EC.nOfWC):
                self.WC.playFunc(self)
        self.addlinetoCSVF()
        return (self)



 
    def printCSVHeader(self):
        print("roundnr,stepnr,player,A,B,C,Total,winer,ec,ecset,nofworms,wcs,wormset;")
        return (True)
    
 

    def addlinetoCSVF(self):
        PV = (self.P.playerVars)
        # cleaning before writing
        if len(self.P.PCStatus) == 0:
            playerPCStatus = ''
        else:
            playerPCStatus = self.P.PCStatus
        #----
        if len(PV.Nullindex)==0:
                nullList=''
        else:
            nullList = str(PV.Nullindex)
        #-----
        if len(self.WC.playedWCName)==0:
            playedWCName = ''
        else:
            playedWCName = self.WC.playedWCName

        #writing in file
        rowlist = [self.roundNr,self.stepNr,self.P.Name, PV.varsValue[0], PV.varsValue[1], PV.varsValue[2]]
        rowlist = rowlist + [PV.varsValue[3], nullList , self.EC.currentEC,self.EC.nOfWC]
        rowlist = rowlist+ [self.playerDesicion ,playerPCStatus, self.P.roundCounter]
        rowlist = rowlist + [self.EC.ECName, playedWCName,self.winer,self.EC.playedEC, self.WC.playedWC]
        with open('gameData2.csv', 'a+', newline='') as f:
            csvwriter = writer(f,delimiter=';')
            csvwriter.writerow(rowlist)        
        f.close()
        return True