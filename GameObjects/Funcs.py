import copy
from GameObjects.MainRAMVars import *


class Funcs(object):
    """description of class"""
    def __init__(self,vars,funcslist,varnumber, value):
        self.PV = copy.deepcopy(vars)
        self.playingfuncs = funcslist
        self.varnumber = varnumber
        self.value = value
        return
    
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
