#from enum import Enum
from random import randrange
import copy
import numpy as np
#from GameObjects.Player import *
from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *
#0 to 5 task functions# 
#6 to 9 input functions
#10 to 30 resource functions
class EventCards():
    """description of class"""
    GS = GameSettings()
    PV = MainRAMVars()
    playedCardsSet = set()
    reservedCardsSet =set()
    ECName = ''
    a = np.array(PV.VarsValue)    
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
        return
    def selectVar(self):
       if len(self.PV.Nullindex)>0:     
            #pop remove item and get its value
            r = self.PV.Nullindex.pop(0)
       else: 
            try:
                r = self.PV.VarsValue.argmin()
                #r = self.PV.VarsValue.index(x)
            except ValueError:
                r=0
       return r
    def checknull(self,ind,add):
        check = False
        if 3  in self.PV.Nullindex:                
                check = True
        else:
            a= any(item in ind for item in self.PV.Nullindex)
            if   a==True:
                check= True
                if add== True:
                    self.PV.Nullindex.append(3)
            
        return check        
             
                 
        return (check)
    # list of Cards
    #-------------------
    #A: input Cards
    #-------------------
    # 2 digit number
    def ECFunc0(self):
        self.ECName = 'EC:Input:2 digit number'
        n = randrange(100)
        i = self.selectVar()
        self.PV.VarsValue[i] = n  
        self.nOfWC = 1
        return(self)

    # 2 digit number less than 50   
    def ECFunc1(self):
        self.ECName = 'EC:Input:2 digit number<50'
        n = randrange(50)
        i = self.selectVar()
        self.PV.VarsValue[i] = n         
        self.nOfWC = 1
        return(self)

    # 2 digit number less than 90       
    def ECFunc2(self):
        self.ECName = 'EC:Input:2 digit number<90'
        n = randrange(90)
        i = self.selectVar()
        self.PV.VarsValue[i] = n
        self.nOfWC = 1
        return(self)
    # 2 digit number less than 30    
    def ECFunc3(self):
        self.ECName = 'EC:Input:2 digit number<30'
        n = randrange(30)
        i = self.selectVar()
        self.PV.VarsValue[i] = n
        self.nOfWC = 0
        return(self)
    
    # A =5    
    def ECFunc4(self):
        self.ECName = 'EC:Input:A =5'
        self.PV.VarsValue[0] = 5
        self.nOfWC = 0
        return(self)
    # A =10    
    def ECFunc5(self):
        self.ECName = 'EC:Input:A =10'
        self.PV.VarsValue[0] = 10
        self.nOfWC = 0
        return(self)
      # A =25    
    def ECFunc6(self):
        self.ECName = 'EC:Input:A =25'
        self.PV.VarsValue[0] = 25
        self.nOfWC = 0
        return(self)
    # A =50    
    def ECFunc7(self):
        self.ECName = 'EC:Input:A =50'
        self.PV.VarsValue[0] = 50
        self.nOfWC = 0
        return(self)
    # A =75    
    def ECFunc8(self):
        self.ECName = 'EC:Input:A =75'
        self.PV.VarsValue[0] = 75
        self.nOfWC = 0
        return(self)
  
    # sum of the dice of all players
    def ECFunc9(self):
        self.ECName = 'EC:Input: sum dice of all players'
        a = 0
        for i in range(self.GS.NrOfP):
            a = a + randrange(6)
        var = self.selectVar()
        self.PV.VarsValue[var] = a
        self.nOfWC = 0
        return(self)
    # B = 10
    def ECFunc10(self):
        self.ECName = 'EC:Input:B =10'
        self.PV.VarsValue[1] = 10  
        self.nOfWC = 0
        return(self)
    # B= 20
    def ECFunc11(self):
        self.ECName = 'EC:Input:B =20'
        self.PV.VarsValue[1] = 20
        self.nOfWC = 0
        return(self)
    # B=30
    def ECFunc12(self):
        self.ECName = 'EC:Input:B =30'
        self.PV.VarsValue[1] = 30  
        self.nOfWC = 0
        return(self)
    # B=50
    def ECFunc13(self):
        self.ECName = 'EC:Input:B =50'
        self.PV.VarsValue[1] = 50  
        self.nOfWC = 0
        return(self)
    # B=70
    def ECFunc14(self):
        self.ECName = 'EC:Input:B =70'
        self.PV.VarsValue[1] = 70  
        self.nOfWC = 1
        return(self)
    # C=5
    def ECFunc15(self):
        self.ECName = 'EC:Input:C =5'
        self.PV.VarsValue[2] = 5  
        self.nOfWC = 0
        return(self)
    # C=15
    def ECFunc16(self):
        self.ECName = 'EC:Input:C =15'
        self.PV.VarsValue[2] = 15
        self.nOfWC = 0
        return(self)
    # C=25
    def ECFunc17(self):
        self.ECName = 'EC:Input:C =25'
        self.PV.VarsValue[2] = 25  
        self.nOfWC = 0
        return(self)
    # C=45
    def ECFunc18(self):
        self.ECName = 'EC:Input:C =45'
        self.PV.VarsValue[2] = 45  
        self.nOfWC = 0
        return(self)
    # C=75
    def ECFunc19(self):
        self.ECName = 'EC:Input:C =75'
        self.PV.VarsValue[2] = 75  
        self.nOfWC = 1
        return(self)
    #-------------------
    #Task cards functions
    #-------------------

    def ECFunc20(self):
        self.ECName = 'EC:Task: T += A+B'
        ind= [0,1,3]
        if not self.checknull(ind,True):
                self.PV.VarsValue[3] = np.sum(self.PV.VarsValue[ind])
        self.nOfWC = 1   
        return(self)

    def ECFunc21(self):
        self.ECName = 'EC:Task: T = A*B'
        ind = [0,1]
        if not self.checknull(ind,False):
            self.PV.VarsValue[3] = self.PV.VarsValue[0] * self.PV.VarsValue[1]
        self.nOfWC = 1   
        return(self)

    def ECFunc22(self):
        self.ECName = 'EC:Task: T += A+B+C'
        ind =[0,1,2,3]   
        if not self.checknull(ind,True):
            self.PV.VarsValue[3] = sum(self.PV.VarsValue)
        self.nOfWC = 1   
        return(self)

    def ECFunc23(self):
        self.ECName = 'EC:Task: T = xx9x'
        ind =[3]
        if not self.checknull(ind,False):
            t = self.PV.VarsValue[3]
            strt = str(t)
            a= strt[0]
            b= strt[2:3]
            strt =a+ '9'+ b
            self.PV.VarsValue[3] = int(strt)
        self.nOfWC = 1   
        return(self)
   
    def ECFunc24(self):
        self.ECName = 'EC:Task: T += sum all/2'
        ind = [0,1,2]
        
        if not self.checknull(ind,True):
            self.PV.VarsValue[3] = self.PV.VarsValue[3]+np.sum(self.PV.VarsValue[ind])/2
        self.nOfWC = 2  
        return(self)

    def ECFunc25(self):
        self.ECName = 'EC:Task: T += sum all'
        ind =[0,1,2,3]
        if not self.checknull(ind,True):
            self.PV.VarsValue[3] = sum(self.PV.VarsValue)
        self.nOfWC = 2
        return(self)

    def ECFunc26(self):
        self.ECName = 'EC:Task: T += B+(2*A)'
        ind = [3,1]
        indif =[3,1,2]
        if not self.checknull(indif,True):    
            self.PV.VarsValue[3]=np.sum(self.PV.VarsValue[ind])+(self.PV.VarsValue[0]*2)
        self.nOfWC = 2
        return (self)

    def ECFunc27(self):
        self.ECName = 'EC:Task: T += 2*(A+B+C)'
        ind = [0,1,2]
        indif = [0,1,2,3]
        if not self.checknull(indif,True):
             self.PV.VarsValue[3]=np.sum(self.PV.VarsValue[ind])+(self.PV.VarsValue[3])
        self.nOfWC = 2
        return self
   
    def ECFunc27(self):
        self.ECName = 'EC:Task: x = 2x ! total'
        indif = [0,1,2,3]
        if not self.checknull(indif,True):
            self.PV.VarsValue[0]=self.PV.VarsValue[0]*2
            self.PV.VarsValue[1]=self.PV.VarsValue[1]*2
            self.PV.VarsValue[2]=self.PV.VarsValue[2]*2
        self.nOfWC = 2
        return self
    
    #-------------------
    #resource functions
    #-------------------
    def ECFunc28(self):
#        if (self.GS.GameHardware.CPU2 not in self.hardware):
        self.resourceEC.append(self.GS.ResourceECTypes.Restart)
        self.reservedCardsSet.add(7)
        return(self)

    def ECFunc29(self):
        self.resourceEC.append(self.GS.ResourceECTypes.Freelancer)
        self.reservedCardsSet.add(8)
        return(self)
    