import copy
import random
from GameObjects.MainRAMVars import *


class Funcs(object):
    """description of class"""
    def __init__(self,vars,funcslist,varnumber, value):
        self.PV = copy.deepcopy(vars)
        self.playingfuncs = funcslist
        self.varnumber = varnumber
        self.value = value
        self.funclist = [0,1,2,3]
        return
    #-------------------
    #player functions
    #0: zero instead of null
    #1: absolute value
    #2: add instead of reduce
    #3: add instead of assign
    #-------------------
    
    def updateRAMwithFunc(self,funcnumber):
        if funcnumber == 0:
            self.PV.Nullindex.clear()
        if funcnumber == 1:
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
        funclist = self.funclist
        if ((self.PV.varsValue[3]>=16) or (self.PV.sumvars>=16))and(len(self.playingfuncs) < len(self.funclist)):
            
            fnumber = random.choice(funclist)
            while (fnumber in self.playingfuncs) and (len(funclist)>0):
                funclist.remove(fnumber)
                fnumber = random.choice(funclist)
            if self.PV.varsValue[3] >= 16:
                self.PV.varsValue[3] = self.PV.varsValue[3]-16
                self.playingfuncs.append(fnumber)
                self.updateRAMwithFunc(fnumber)
            else:
                price = 16
                #temp = 0
                if self.PV.varsValue[0]>0 and 0 not in self.PV.Nullindex:
                    price = self.PV.varsValue[0]-price
                    if price == 0:
                        self.PV.varsValue[0]=0
                        self.playingfuncs.append(fnumber)
                        self.updateRAMwithFunc(fnumber)
                        return True
                    elif price>0:
                        self.playingfuncs.append(fnumber)
                        self.PV.varsValue[0]= price
                        self.updateRAMwithFunc(fnumber)
                        return True
                    else:
                        self.PV.varsValue[0] = 0
                        price = (-1*price)
                if self.PV.varsValue[1]>0 and (1 not in self.PV.Nullindex):        
                        price = self.PV.varsValue[1]-price
                        if price == 0:
                            self.PV.varsValue[1]=0
                            self.playingfuncs.append(fnumber)
                            self.updateRAMwithFunc(fnumber)
                            return True
                        elif price>0:
                            self.playingfuncs.append(fnumber)
                            self.PV.varsValue[1]= price
                            self.updateRAMwithFunc(fnumber)
                            return True
                        else:
                            self.PV.varsValue[1] = 0
                            price = (-1*price)
                if self.PV.varsValue[2]>0 and (2 not in self.PV.Nullindex):        
                        price = self.PV.varsValue[2]-price
                        if price == 0:
                            self.PV.varsValue[2]=0
                            self.playingfuncs.append(fnumber)
                            self.updateRAMwithFunc(fnumber)

                            return True
                        elif price>0:
                            self.playingfuncs.append(fnumber)
                            self.PV.varsValue[2]= price
                            self.updateRAMwithFunc(fnumber)
                            return True
        else:
            return False
        return True
    
    def playallFuncs(self):
        pf = self.playallFuncs
        while len(pf)>0:
            FuncName = 'ECFunc' + str(pf.pop())
            getattr(self, FuncName)()
        return self

    def func0(self):
        #zero instead of null
        if self.varnumber in self.PV.Nullindex:
            Nullindex.remove(varnumber)
        return 

    def func1(self):
        #Absolut value
        if self.value <0:
           self.value = -1 * self.value
        return 
    
    def func2(self):
        #Add isntead of asign
        if self.varnumber not in self.PV.nullindex:
            self.PV.varsValue[self.varnumber] = self.PV.varsValue[self.varnumber] + self.value
        return 

    def func3(self):
        #add instead of reduce
        if self.value <0:
           self.value = -1 * self.value
        return 
