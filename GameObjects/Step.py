#for file
import tempfile
import itertools as IT
import os
#------
from GameObjects.Game import *
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from GameObjects.Player import *
from GameObjects.desicion import *
import copy
import csv
from csv import writer
from datetime import datetime
from collections import Counter



class Step():
    """Status of each step of game, it is like a copy of variable to save the result  at one place"""
    def __init__(self,*args,**kwargs):     
        self.winer = ''
        # self.GS = kwargs.get('gamesettings',GameSettings())        
        # it is 0 to produce error instead of initializing empty  gamesettings obj.
        GD = kwargs.get('currentgamedeck',0)        
        self.P = kwargs.get('p',Player('N'))
        #pv = copy.deepcopy(self.P.playerVars)
        self.WC = WormCards(self.P.playerVars,GD,self.P.playerfuncs)
        self.EC = EventCards(self.P.playerVars,self.P.PlayerReservedEC,GD,self.P.playerfuncs)
        self.currentMixedCards = GD.currentMixedCards
        self.initialMixedCards = GD.initialMixedCards
        #self.playerDesicion = False
        #self.myDesicion = desicion()
        #
        #only to write in DB/file, etc.
        self.roundNr = kwargs.get('currentRound',0)
        self.stepNr = kwargs.get('currentStep',0)
        return

    def updatePlayer(self, afterstr):
        if afterstr == 'WC':
            self.P.playerVars = copy.deepcopy(self.WC.PV) 
            self.P.PCStatus = self.WC.damages
            self.P.nofRoundPausing = self.WC.nofRoundspausing

        if afterstr == 'EC':
            self.P.playerfuncs = self.EC.playerfuncs
            self.P.playerVars = self.EC.PV

        #general
        self.P.playerVars.sumvars = self.P.playerVars.calculatesumvars()

        return self

    #-------------------------
    #-------------------------
    def playWC(self):
        self.WC.playFunc(self)
        self.updatePlayer()
        return self
    
    def playOneStep(self):
        total = 0 
        GS = GameSettings()
        #should change: sel 
        d = desicion()._init_(self.P)
        d.playerdesicion()
        self.P.update_afterdecision(d)
        #self.P = copy.deepcopy(d.playerdesicion().player)
        if (len(self.currentMixedCards) == 0):
            self.currentMixedCards = self.initialMixedCards.deck
            self.currentMixedCards.shuffle()
            
        currentCard = self.currentMixedCards[0]
        self.currentMixedCards = np.delete(self.currentMixedCards,[0])

        if self.P.mydesicion:
            if currentCard<5000:
                self.EC.currentEC = currentCard
                self.EC.playFunc(self)
                #self= copy.deepcopy(self.EC.playFunc(self))    
                self.updatePlayer('EC')
                if (GS.ifWined(self.P.playerVars.varsValue[3])):
                    self.winer = self.P.Name
                    return (self)
            else:
       # for i in range(self.EC.nOfWC):
            #self = copy.deepcopy(d.playerdesicion())
                d = desicion()._init_(self.P)
                d.playerdesicion()
                self.P.update_afterdecision(d)
                if (self.P.mydesicion):
                    self.WC.currentWC = currentCard-5000
                    self.WC.playFunc(self)
                    self.updatePlayer('WC')
                    a = self.P.playerVars
        return (self)
 
    def writeCSVHeader(self, file):
       # rowlist =['roundnr','stepnr','player','A:0','B:1','C:2','Total:3','NULL vars',	'ec']
        rowlist = rowlist + ['nofworms','my decision',	'PC Status', 'count down paus',	'EC Name']
        rowlist = rowlist + ['WC Name',	'Winner	ecset',	'wormset']
        csvwriter = writer(file,delimiter=';')
        csvwriter.writerow(rowlist)
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
        #rowlist = [self.roundNr,self.stepNr,self.P.Name, PV.varsValue[0], PV.varsValue[1], PV.varsValue[2]]
        rowlist = rowlist + [PV.varsValue[3], nullList , self.EC.currentEC,self.EC.nOfWC]
        #rowlist = rowlist+ [self.playerDesicion ,playerPCStatus, self.P.roundCounter]
        rowlist = rowlist + [self.EC.ECName, playedWCName,self.winer,self.EC.playedEC, self.WC.playedWC]
        now = datetime.now() # current date and time
        fName = 'generated data/sample-'+str(self.sampleNr)+'-'+ str(self.GS.NrOfP) +'player'+now.strftime("%Y")
        fName = fName+now.strftime("%m")+now.strftime("%Y")+now.strftime("%H%M")+'.csv'
        with open(fName, 'a+', newline='') as f:
            if self.stepNr == 0 :
                self.writeCSVHeader(f)
            csvwriter = writer(f,delimiter=';')
            csvwriter.writerow(rowlist)        
        f.close()
        return True

    def printStep(self):
        print("step information")
        print(self.stepNr)
        #print("reserved cards" + str(self.reservedEC))
        self.P.printMainRAM()                 
        #print(self.playerDesicion)         
        return

def uniquify(path, sep = ''):
    def name_sequence():
        count = IT.count()
        yield ''
        while True:
            yield '{s}{n:d}'.format(s = sep, n = next(count))
    orig = tempfile._name_sequence 
    with tempfile._once_lock:
        tempfile._name_sequence = name_sequence()
        path = os.path.normpath(path)
        dirname, basename = os.path.split(path)
        filename, ext = os.path.splitext(basename)
        fd, filename = tempfile.mkstemp(dir = dirname, prefix = filename, suffix = ext)
        tempfile._name_sequence = orig
    return filename

 