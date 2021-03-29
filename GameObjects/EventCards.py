from random import randrange
import copy
import numpy as np
from GameObjects.MainRAMVars import *
from GameObjects.GameSettings import *

class EventCards():
    """description of class"""    

    def __init__(self,vars,pec,resEC,rec):
        self.PV = copy.deepcopy(vars)
        self.currentEC = 0
        self.playedEC = pec
        self.reservedEC = resEC
        self.resourceEC = rec
        self.GS = GameSettings()
        self.ECName = ''
        self.nOfWC = 0
        return

    def updateEC(self, vars,pc,rc):
        self.PV = copy.deepcopy(vars)
        self.playedEC = pc
        self.reservedEC = rc
        return self

    def update_Vars(self,vars):
        self.PV = copy.deepcopy(vars)
        return self

    def SelectNextEC(self):
        self.reset()
        if len(self.playedEC)==0:
            self.playedEC = {self.currentEC}
        else:
            while ((self.currentEC in self.playedEC) or (self.currentEC in self.reservedEC)):
                self.currentEC = randrange(self.GS.NrofEC)        
            self.playedEC.add(self.currentEC)        
        return self
    
    def reset(self):
        #self.sumPlayedEC = self.sumPlayedEC+1
        if (len(self.playedEC) == self.GS.NrofEC):
            self.playedEC.clear()
            self.playedEC = copy.deepcopy(self.reservedEC)
        return(self)
    def asignVar(self,var,value):
        if var in self.PV.Nullindex:
            self.PV.Nullindex.remove(var)
        self.PV.varsValue[var]=value
        return
            
    def unreserve(self,ec):
        self.reservedEC.discard(ec)
        return

    def selectVar(self):
        vars = copy.deepcopy(self.PV)
        #total should be removed from vars selection
        vars.varsValue = copy.deepcopy(self.PV.varsValue[:3])
#        np.delete(vars.varsValue,3,0)
        if 3 in vars.Nullindex:
            vars.Nullindex.remove(3)
        print(self.ECName)
        print("nullindex")
        print(vars.Nullindex)
        print("varvalues")
        print(vars.varsValue)
        if len(vars.Nullindex)>0:     
            #pop remove item and get its value
            r = vars.Nullindex.pop(0)
        else: 
            try:
                r = vars.varsValue.argmin()
            except ValueError:
                r=0
        return r
   #name should change because it choose variable
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
            
       # return check        
             
                 
        return (check)
    
    def playFunc(self,s):
        """calling a function with making its name as string"""  
        self.updateEC(s.P.playerVars,s.playedEC, s.reservedEC)
        self.SelectNextEC()
        FuncName = 'ECFunc' + str(self.currentEC)
        getattr(self, FuncName)()
        s.P.updatePlayer(self.PV)
        return s

    # list of Cards
    #-------------------
    #A: input Cards
    #-------------------
    # 2 digit number
    def ECFunc0(self):
        self.ECName = 'EC:Input:2 digit number'
        n = randrange(100)
        i = self.selectVar()
        self.asignVar(i,n)
#        self.PV.varsValue[i] = n  
        self.nOfWC = 1
        return(self)

    # 2 digit number less than 50   
    def ECFunc1(self):
        self.ECName = 'EC:Input:2 digit number<50'
        n = randrange(50)
        i = self.selectVar()
        self.asignVar(i,n)
#        self.PV.varsValue[i] = n         
        self.nOfWC = 1
        return(self)

    # 2 digit number less than 90       
    def ECFunc2(self):
        self.ECName = 'EC:Input:2 digit number<90'
        n = randrange(90)
        i = self.selectVar()
        self.asignVar(i,n)
        #self.PV.varsValue[i] = n
        self.nOfWC = 1
        return(self)
    # 2 digit number less than 30    
    def ECFunc3(self):
        self.ECName = 'EC:Input:2 digit number<30'
        n = randrange(30)
        i = self.selectVar()
        self.asignVar(i,n)
        #self.PV.varsValue[i] = n
        self.nOfWC = 0
        return(self)
    
    # A =5    
    def ECFunc4(self):
        self.ECName = 'EC:Input:A =5'
        self.asignVar(0,5)
        #self.PV.varsValue[0] = 5
        self.nOfWC = 0
        return(self)
    # A =10    
    def ECFunc5(self):
        self.ECName = 'EC:Input:A =10'
        self.asignVar(0,10)
        #self.PV.varsValue[0] = 10
        self.nOfWC = 0
        return(self)
      # A =25    
    def ECFunc6(self):
        self.ECName = 'EC:Input:A =25'
        self.asignVar(0,25)
        #self.PV.varsValue[0] = 25
        self.nOfWC = 0
        return(self)
    # A =50    
    def ECFunc7(self):
        self.ECName = 'EC:Input:A =50'
        #self.PV.varsValue[0] = 50
        self.asignVar(0,50)
        self.nOfWC = 0
        return(self)
    # A =75    
    def ECFunc8(self):
        self.ECName = 'EC:Input:A =75'
        self.asignVar(0,75)
        #self.PV.varsValue[0] = 75
        self.nOfWC = 0
        return(self)
  
    # sum of the dice of all players
    def ECFunc9(self):
        self.ECName = 'EC:Input: sum dice of all players'
        a = 1
        for i in range(self.GS.NrOfP):
            a = a + randrange(6)
        var = self.selectVar()
        self.PV.varsValue[var] = a
        self.nOfWC = 0
        return(self)
    # B = 10
    def ECFunc10(self):
        self.ECName = 'EC:Input:B =10'
        self.asignVar(1,10)
        #self.PV.varsValue[1] = 10  
        self.nOfWC = 0
        return(self)
    # B= 20
    def ECFunc11(self):
        self.ECName = 'EC:Input:B =20'
        self.asignVar(1,20)
        #self.PV.varsValue[1] = 20
        self.nOfWC = 0
        return(self)
    # B=30
    def ECFunc12(self):
        self.ECName = 'EC:Input:B =30'
        self.asignVar(1,30)
        #self.PV.varsValue[1] = 30  
        self.nOfWC = 0
        return(self)
    # B=50
    def ECFunc13(self):
        self.ECName = 'EC:Input:B =50'
        self.asignVar(1,50)
        #self.PV.varsValue[1] = 50  
        self.nOfWC = 0
        return(self)
    # B=70
    def ECFunc14(self):
        self.ECName = 'EC:Input:B =70'
        self.asignVar(1,70)
        #self.PV.varsValue[1] = 70  
        self.nOfWC = 1
        return(self)
    # C=5
    def ECFunc15(self):
        self.ECName = 'EC:Input:C =5'
        self.asignVar(2,5)
        #self.PV.varsValue[2] = 5  
        self.nOfWC = 0
        return(self)
    # C=15
    def ECFunc16(self):
        self.ECName = 'EC:Input:C =15'
        self.asignVar(2,15)
        #self.PV.varsValue[2] = 15
        self.nOfWC = 0
        return(self)
    # C=25
    def ECFunc17(self):
        self.ECName = 'EC:Input:C =25'
        self.asignVar(2,25)
        #self.PV.varsValue[2] = 25  
        self.nOfWC = 0
        return(self)
    # C=45
    def ECFunc18(self):
        self.ECName = 'EC:Input:C =45'
        self.asignVar(2,45)
        #self.PV.varsValue[2] = 45  
        self.nOfWC = 0
        return(self)
    # C=75
    def ECFunc19(self):
        self.ECName = 'EC:Input:C =75'
        self.asignVar(2,75)
        #self.PV.varsValue[2] = 75  
        self.nOfWC = 1
        return(self)
    #-------------------
    #Task cards functions
    #-------------------

    def ECFunc20(self):
        self.ECName = 'aEC:Task: T += A+B'
        ind= [0,1,3]
        if not self.checknull(ind,True):
                self.PV.varsValue[3] = np.sum(self.PV.varsValue[ind])
        self.nOfWC = 1   
        return(self)

    def ECFunc21(self):
        self.ECName = 'EC:Task: T = A(*)+B'
        ind = [0,1]
        if not self.checknull(ind,False):
            self.PV.varsValue[3] = self.PV.varsValue[0] + self.PV.varsValue[1]
        self.nOfWC = 1   
        return(self)

    def ECFunc22(self):
        self.ECName = 'EC:Task: T += A+B+C'
        ind =[0,1,2,3]   
        if not self.checknull(ind,True):
            self.PV.varsValue[3] = sum(self.PV.varsValue)
        self.nOfWC = 1   
        return(self)

    def ECFunc23(self):
        self.ECName = 'EC:Task: T = xx9x'
        ind =[3]
        if not self.checknull(ind,False):
            t = self.PV.varsValue[3]
            strt = str(t)
            a= strt[0]
            b= strt[2:3]
            strt =a+ '9'+ b
            self.PV.varsValue[3] = int(strt)
        self.nOfWC = 1   
        return(self)
   
    def ECFunc24(self):
        self.ECName = 'EC:Task: T += sum all/2'
        ind = [0,1,2]
        
        if not self.checknull(ind,True):
            self.PV.varsValue[3] = self.PV.varsValue[3]+np.sum(self.PV.varsValue[ind])/2
        self.nOfWC = 2  
        return(self)

    def ECFunc25(self):
        self.ECName = 'EC:Task: T += sum all'
        ind =[0,1,2,3]
        if not self.checknull(ind,True):
            self.PV.varsValue[3] = sum(self.PV.varsValue)
        self.nOfWC = 2
        return(self)

    def ECFunc26(self):
        self.ECName = 'EC:Task: T += B+((2*)A)'
        ind = [3,1]
        indif =[3,1,2]
        if not self.checknull(indif,True):    
            self.PV.varsValue[3]=np.sum(self.PV.varsValue[ind])+(self.PV.varsValue[0])
        self.nOfWC = 2
        return (self)

    def ECFunc27(self):
        self.ECName = 'EC:Task: T += (2*)(A+B+C)'
        ind = [0,1,2]
        indif = [0,1,2,3]
        if not self.checknull(indif,True):
             self.PV.varsValue[3]=np.sum(self.PV.varsValue[ind])+(self.PV.varsValue[3])
        self.nOfWC = 2
        return self
   
    def ECFunc27(self):
        self.ECName = 'EC:Task: x = 2x ! total'
        indif = [0,1,2]
        if not self.checknull(indif,True):
            self.PV.varsValue[0]= (self.PV.varsValue[0]) * 2
            self.PV.varsValue[1]= (self.PV.varsValue[1]) * 2
            self.PV.varsValue[2]= (self.PV.varsValue[2]) * 2
        self.nOfWC = 2
        return self
    
    #-------------------
    #resource functions
    #-------------------
    def ECFunc28(self):
        self.ECName = 'EC:Resource: Restart'
        self.resourceEC.append(self.GS.ResourceECTypes.Restart)
        self.reservedEC.add(28)
        return(self)

    def ECFunc29(self):
        self.ECName = 'EC:Resource: Freelancer'
        self.resourceEC.append(self.GS.ResourceECTypes.Freelancer)
        self.reservedEC.add(29)
        return(self)

    def ECFunc30(self):
        self.ECName = 'EC:Resource: Bazar'
        self.resourceEC.append(self.GS.ResourceECTypes.Bazar)
        self.reservedEC.add(30)
        return(self)
#copy of functions  
    def ECFunc31(self):
        self.ECName = 'EC:Resource: Restart'
        self.resourceEC.append(self.GS.ResourceECTypes.Restart)
        self.reservedEC.add(28)
        return(self)
    def ECFunc32(self):
        self.ECName = 'EC:Resource: Restart'
        self.resourceEC.append(self.GS.ResourceECTypes.Restart)
        self.reservedEC.add(28)
        return(self)
    def ECFunc33(self):
        self.ECName = 'EC:Resource: Restart'
        self.resourceEC.append(self.GS.ResourceECTypes.Restart)
        self.reservedEC.add(28)
        return(self)