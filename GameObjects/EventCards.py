#from enum import Enum
from random import randrange
import copy
#from GameObjects.Player import *
from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *
#0 to 5 task functions
#6 to 9 input functions
#10 to 30 resource functions
class EventCards():
    """description of class"""
    GS = GameSettings()
    PV = MainRAMVars()
    playedCardsSet = set()
    reservedCardsSet =set()
    
    hardware= []
    # initial which resource is added after playing an EC card
    resourceEC = []
    currentEC = 0
    nOfWC= 0

    def SelectNextEC(self):
        self.reset()
        if len(self.playedCardsSet)==0:
            self.playedCardsSet = {self.currentEC}
        else:
            while ((self.currentEC in self.playedCardsSet) or (self.currentEC in self.reservedCardsSet)):
                self.currentEC = randrange(self.GS.NrofEC)        
            self.playedCardsSet.add(self.currentEC)        
        return self.currentEC
    
    def reset(self):
        #self.sumPlayedEC = self.sumPlayedEC+1
        if (len(self.playedCardsSet) == self.GS.NrofEC):
            self.playedCardsSet.clear()
            self.playedCardsSet = copy.deepcopy(self.reservedCardsSet)
        return(self)
    def unreserve(self,ec):
        self.reservedCardsSet.discard(ec)

    def selectVar(self):
        try:
            r = self.PV.NullVars.index('N')
        except ValueError:
            try:
                x = min(self.PV.VarsValue)
                r = self.PV.VarsValue.index(x)
            except ValueError:
                r=0
        return r

    # list of Cards
    # 2 digit number
    def ECFunc0(self):
        n = randrange(100)
        i = self.selectVar()
        self.PV.VarsValue[i] = n 
        self.nOfWC = 1
        return(self)

    # 2 digit number less than 50   
    def ECFunc1(self):
        n = randrange(50)
        i = self.selectVar()
        self.PV.VarsValue[i] = n         
        self.nOfWC = 1
        return(self)

    # 2 digit number less than 90       
    def ECFunc2(self):
        n = randrange(90)
        i = self.selectVar()
        self.PV.VarsValue[i] = n
        self.nOfWC = 1
        return(self)
    # 2 digit number less than 30    
    def ECFunc3(self):
        n = randrange(30)
        i = self.selectVar()
        self.PV.VarsValue[i] = n
        self.nOfWC = 0
        return(self)
    
    # A =5    
    def ECFunc4(self):
        self.PV.VarsValue[0] = 5
        self.nOfWC = 0
        return(self)
    
    
    def ECFunc5(self):
        self.PV.VarsValue[3] = self.PV.VarsValue[3] + self.PV.VarsValue[0]+ self.PV.VarsValue[1] + self.PV.VarsValue[2]
        if self.PV.VarsValue[3] < 0:
            self.PV.VarsValue[3] = -1* self.PV.VarsValue[3]
        self.nOfWC = 1
        return(self)

    def ECFunc6(self):
        self.PV.VarsValue[2] = 2  
        self.nOfWC = 2
        return(self)

    def ECFunc7(self):
        self.PV.VarsValue[1] = 5
        self.nOfWC = 0
        return(self)
    # input functions 
    def ECFunc8(self):
        self.PV.VarsValue[2] = 2  
        self.nOfWC = 0
        return(self)
    #resource functions
    def ECFunc10(self):
#        if (self.GS.GameHardware.CPU2 not in self.hardware):
        self.resourceEC.append(self.GS.ResourceECTypes.Restart)
        self.reservedCardsSet.add(7)
        return(self)
    def ECFunc11(self):
        self.resourceEC.append(self.GS.ResourceECTypes.Freelancer)
        self.reservedCardsSet.add(8)
        return(self)
    def ECFunc9(self):
        self.PV.VarsValue[3] = self.PV.VarsValue[3] + self.PV.VarsValue[0]+ self.PV.VarsValue[1] + self.PV.VarsValue[2]
        if self.PV.VarsValue[3] < 0:
            self.PV.VarsValue[3] = -1* self.PV.VarsValue[3]
        self.nOfWC = 1
        return(self)
  
    #adding hardware to pc of player
    #def ECFunc9(self):
     #   if (self.GS.GameHardware.SSD not in self.hardware):
      #      self.hardware.append(self.GS.GameHardware.SSD)
       # return(self)
            
