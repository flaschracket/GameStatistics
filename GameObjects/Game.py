from GameObjects.GameSettings import *
from GameObjects.Step import *
from GameObjects.MainRAMVars import *
from GameObjects.Player import *
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from random import randrange
import copy
import csv
from csv import writer

class Game():
    """description of class"""
    const = GameSettings()
    winer = ''
    nofPlayers = 0
    currentRound = 0
    currentEC = 0
    currentWC = 0
    currentWormsSet = {}
    currentStep = 0
    #currentPenalty = 0
    currentPlayer = Player()
    listofPlayers = []
    listofSteps = []
    EC = EventCards()
    WC = WormCards()
    DE = GameSettings()
    

    

    def ifWined(self):
        wined= False
        if (self.currentPlayer.PlayerVars.Total > self.DE.winGoal):
            wined = True
            self.winer = self.currentPlayer.Name
        return (self)
    
    def playEC(self):
        """calling a function with making its name as string"""
        self.currentEC = self.EC.SelectNextEC()
        self.EC.PV = copy.deepcopy(self.currentPlayer.PlayerVars)
        FuncName = 'ECFunc' + str(self.currentEC)
        getattr(self.EC, FuncName)()
        self.currentPlayer.PlayerVars = copy.deepcopy(self.EC.PV)
        #self.printgame("PlayEC")
        return(self)

    def playWC(self):
        self.WC.SelectNextWC()
        self.WC.PV = copy.deepcopy(self.currentPlayer.PlayerVars)
        FuncName = 'WCFunc' + str(self.WC.currentWC)
        funcresult = getattr(self.WC, FuncName)()
        self.currentPlayer.PlayerVars = copy.deepcopy(self.WC.PV)
        #OMGCorruption(self,myturn)
        return (self)

    def playOneStep(self):
        self.playEC()
        self.ifWined()
        #self.EC.playedCardsSet.add(self.currentEC)
        if (self.winer != ''):
            self.Stepsnapshot()
            #s = copy.deepcopy(self.Stepsnapshot())    
            return (self)
        for i in range(self.EC.nOfWC):
            self.playWC()
        self.Stepsnapshot()
        self.listofSteps[self.currentStep].addlinetoCSVF()
        #self.printgame("step")
        self.currentStep = self.currentStep+1
        return (self)
    
    def playOneRound(self):
        for x in range(self.nofPlayers):
            self.currentPlayer = copy.deepcopy(self.listofPlayers[x])
            #self.printgame("round1:")
            self.playOneStep()
            #self.printgame("round2:")
            self.listofPlayers[x] = copy.deepcopy(self.currentPlayer)
            if (self.winer != ''):
                break            
            self.currentEC = self.EC.currentEC
        return self

    def Stepsnapshot(self):
        s = Step()
        s.roundNr = self.currentRound
        s.stepNr = self.currentStep
        s.P = copy.deepcopy(self.currentPlayer)        
        #for i in range(self.const.NrOfWC):
        #s.wormSet.add((self.currentWormsSet))
        s.winer = self.winer
#        s.nofcorruption = self.nOfCorruption
        s.playedECset = self.EC.playedCardsSet
#        s.Wormset = self.WC.playedWormCardsSet 
        s.currentEC = copy.deepcopy(self.currentEC)
        s.playedWormsSet = self.WC.playedWormCardsSet
        #print(str(s.playedWormsSet))
        s.nOfWC = self.EC.nOfWC
        self.listofSteps.append(s)
        #self.printgame("stepsnapshot")
        #self.writeCSVfile()
        return self
    def addlinetoCSV(self):
        #f = open('gameData.csv', 'w', newline= '\r\n')
        #w = csv.writer(f, delimiter = ';')    
        
        #fnames = ['roundnr', 'stepnr', 'player', 'A', 'B', 'C', 'Total', 'winer', 'ec', 'ecset', 'nofworms', 'wormset', 'line']
        #{'roundnr' : s.roundNr, 'stepnr': s.stepNr, 'player': s.P.Name, 'A': PV.VarA, 'B': PV.VarB, 'C': PV.VarC, 'Total': PV.Total, 'winer': s.winer, 'ec': s.currentEC, 'ecset': ''.join(str(s.playedECset)), 'nofworms':s.nOfWC, 'wormset':str(s.playedWormsSet), 'line':' aaaaa \n' }
        # if self.currentStep == 0:
        #       csvwriter.writeheader()
        row = self.currentStep-1
        s = copy.deepcopy(self.listofSteps[row])
        PV = (s.P.PlayerVars)
        #rowlist = {str(s.roundNr),str(s.stepNr),s.P.Name, str(PV.VarA), str(PV.VarB),str(PV.VarC), str( PV.Total), str(s.winer), str(s.currentEC), ''.join(str(s.playedECset)),str(s.nOfWC), str(s.playedWormsSet)}
        rowlist = {s.roundNr,s.stepNr,s.P.Name, str(PV.VarA), str(PV.VarB),str(PV.VarC), str( PV.Total), str(s.winer), str(s.currentEC), ''.join(str(s.playedECset)),str(s.nOfWC), str(s.playedWormsSet)}
        print(str(rowlist))
        with open('gameData.csv', 'a+', newline='') as f:
            #writer = csv.DictWriter(f, fieldnames=fnames)
            csvwriter = writer(f)
            csvwriter.writerow(rowlist)        
            #end with f
        f.close()    
        return True
        
    def writeCSVfile(self):
    # there is an error, the software change the values of sets in step array to {}. therefore there is not a last ergebnis.  
        print("first line of csv"+self.listofSteps[1].winer)
        f = open('gameData.csv', 'w')
        w = csv.writer(f, delimiter = ',')
        with f:
            fnames = ['roundnr', 'stepnr', 'player', 'A', 'B', 'C', 'Total', 'winer', 'ec', 'ecset', 'nofworms', 'wormset']
            #fnames = [ 'roundnr', 'player']
            writer = csv.DictWriter(f, fieldnames=fnames) 
            writer.writeheader()
            for row in range(len(self.listofSteps)):
                #self.currentStep = row
                s = copy.deepcopy(self.listofSteps[row])
                PV = (s.P.PlayerVars)
                #self.printgame("csv file")
                ecs = str(s.playedECset)
                wcs = str(s.playedWormsSet)
                #print("row:"+str(row)+":f:"+ecs)
                #print(str(row)+":f:"+ecs)
                writer.writerow({'roundnr' : s.roundNr, 'stepnr': s.stepNr, 'player': s.P.Name, 'A': PV.VarA, 'B': PV.VarB, 'C': PV.VarC, 'Total': PV.Total, 'winer': s.winer, 'ec': s.currentEC, 'ecset': ''.join(str(s.playedECset)), 'nofworms':s.nOfWC, 'wormset':str(s.playedWormsSet)})        
                
    def printgame(self,s):
        print("it is a game print in " +s)
        #print("step nr:"+str(self.listofSteps[1]))
        #print("nr of WCs:"+str(self.EC.nOfWC))
        #print("nr of WCs:"+str(self.nOfWC))
        #print("current player is:", end =" ")
        #print(self.currentPlayer.Name)
        #print("list of players")
        #for i in range(self.nofPlayers):
         #   print(str(i)+":", end =" ")
          #  print(self.listofPlayers[i].Name)
        #for i in range(self.nofPlayers):
            #print(str(i)+ ": ", end="")
            #self.listofPlayers[i].printMainRAM()
        #print("current winer is:"+self.winer)
        # print("playedWC: "+str(self.WC.playedWormCardsSet)+",", end= " ")   
        slen = len(self.listofSteps)
        print("list of steps length:"+str(slen))         
        for i in range(slen):
             print(self.listofSteps[i].P.Name)
             print("playedWC in Step array: "+str(self.listofSteps[i].playedWormsSet)+";")        
             print("playedEC in Steparray: "+str(self.listofSteps[i].playedECset)+";")
        #print("Current WC:" + str(self.currentWC))
