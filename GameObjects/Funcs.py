import copy
import random
from GameObjects.GameSettings import GameSettings
from GameObjects.MainRAMVars import MainRAMVars
from DB.dbBazar import dbBazar

class Funcs(object):
    """description of class"""
    def __init__(self,vars,playerfuncslist,ReservedEC):
        self.PV = copy.deepcopy(vars)
        self.playerFuncs = playerfuncslist
        self.reservedEC = ReservedEC
        self.buyed = 0
        #define static?
        dbb = dbBazar()
        self.funcList = []
        self.funcName = []
        self.funcMainPrice = []
        self.funcSharedPrice = []

        #make an array of each field of table
        bazarlist = dbb.selectAll()     
        self.funcList.append(bazarlist[0])
        self.funcList = self.funcList[0]
        self.funcName.append(bazarlist[1])
        self.funcName = self.funcName[0]
        self.funcMainPrice.append(bazarlist[2])
        self.funcMainPrice = self.funcMainPrice[0]
        self.funcSharedPrice.append(bazarlist[3])
        self.funcSharedPrice = self.funcSharedPrice[0]
        return
    #def __init__(self, playerRef):
     #   self.player = playerRef;
      #  Funcs(self.player.playerVars, self.player.playerFuncs, self.player.playerReservedEC)
       # return
    #-------------------
    #player functions
    #1: zero instead of null
    #2: absolute value
    #3: add instead of reduce
    #4: add instead of assign
    #-------------------
    
    def updateRAMwithFunc(self,funcnumber):       
        if funcnumber == 1:
            for i in self.PV.Nullindex:
                self.PV.varsValue[i]=0
            self.PV.Nullindex.clear()
        if funcnumber == 2:
            if(self.PV.varsValue[0]<0):
                self.PV.varsValue[0] = self.PV.varsValue[0] * (-1)
            if(self.PV.varsValue[1]<0):
                self.PV.varsValue[1] = self.PV.varsValue[1] * (-1)
            if(self.PV.varsValue[2]<0):
                self.PV.varsValue[2] = self.PV.varsValue[2] * (-1)
            if(self.PV.varsValue[3]<0):
                self.PV.varsValue[3] = self.PV.varsValue[3] * (-1)        
        return
    
    def buyFunc(self):        
        fnumber = -1
        x=4
        tempFuncList = []
        tempFuncMainPrice = []
        tempFuncSharedPrice = []
        # make list of functions which player can buy
        for f in range(len(self.funcList)):
            # f begins from 0 and id from 1
            f=f+1
            #1. player does not have it
            if (f not in self.playerFuncs):
                #player has money to buy
                ind = self.funcList.index(f)
                if self.PV.varsValue[3] >= self.funcMainPrice[ind]:
                    tempFuncMainPrice.append(self.funcMainPrice[ind])
                    tempFuncSharedPrice.append(-1)
                    tempFuncList.append(f)
                elif self.PV.sumvars >= self.funcSharedPrice[ind]:
                    tempFuncMainPrice.append(-1)
                    tempFuncSharedPrice.append(self.funcSharedPrice[ind])
                    tempFuncList.append(f)
        #end of for: list of functions player can buy
        #select to buy        
        if (len(tempFuncList)>0):
            fnumber = random.choice(tempFuncList)
            ind = tempFuncList.index(fnumber)
            tempPrice = tempFuncMainPrice[ind]
            tempSharedPrice = tempFuncSharedPrice[ind]
            self.buyed = 1
            isbought = True          
            # null vars are 0- no need to check here
            #pay the price of function from total
            if ( tempPrice > 0):
                self.reducePriceFromTotal(tempPrice)
            else:
                #pay from shared values
                self.reducePriceFromVars(tempSharedPrice)
        else:
            isbought = False

        if isbought == True:
            self.updateRAMwithFunc(fnumber)
            self.playerFuncs.append(fnumber)
            gs =  GameSettings()
            self.reservedEC.remove(gs.freelancer)
        return isbought
   
    def reducePriceFromTotal(self, tempPrice):
        self.PV.varsValue[3] = self.PV.varsValue[3]-tempPrice
        return self

    def reducePriceFromVars(self, tempSharedPrice):
        #reduce from A      
        temp = self.PV.varsValue[0]-tempSharedPrice
        if temp > 0 :
            self.PV.varsValue[0]= temp
            return True
        self.PV.varsValue[0]=0
        if ( tempSharedPrice == 0):
            return True
        temp = ((-1) * temp)
        #reduce from B
        temp = self.PV.varsValue[1]-temp
        if temp > 0 :
            self.PV.varsValue[1]= temp
            return 
        self.PV.varsValue[1]=0
        if temp == 0:
            return 
        temp = ((-1) * temp)
        #reduce from C
        temp = self.PV.varsValue[2]-temp
        if temp > 0 :
            self.PV.varsValue[2]= temp
            return 
        self.PV.varsValue[2]=0
        return 
        return self

    def playallFuncs(self):
        pf = self.playallFuncs
        while len(pf)>0:
            FuncName = 'ECFunc' + str(pf.pop())
            getattr(self, FuncName)()
        return self
   
    #zero instead of null
    def func1(self):
        if self.varnumber in self.PV.Nullindex:
            Nullindex.remove(varnumber)
        return 
   
    #Absolut value
    def func2(self):
        if self.value <0:
           self.value = -1 * self.value
        return 

    #add instead of reduce
    def func3(self):
        if self.value <0:
           self.value = -1 * self.value
        return 

    #Add isntead of asign
    def func4(self,PV,goalVarIndex, addingValue):    
        #should check before
        if goalVarIndex not in self.PV.Nullindex:
            self.PV.varsValue[goalVarIndex] = self.PV.varsValue[goalVarIndex] + self.value
        return 

    