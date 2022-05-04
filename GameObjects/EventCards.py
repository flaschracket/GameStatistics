from random import randrange

import copy
import numpy as np
from collections import Counter
from GameObjects.MainRAMVars import *
from GameObjects.Funcs import *
from GameObjects.GameSettings import *
from GameObjects.Cards import *
from DB.dbCards import *
from GameObjects.desicion import *
from Abbas.DynamicFunc import *

class EventCards(Cards):
    """description of class"""    
    def __init__(self,vars,resEC,currentgamedeck,playerfuncs):
        self.PV = copy.deepcopy(vars)
        self.currentEC = 0
        self.reservedEC = resEC
        self.GS = GameSettings()
        self.ECName = ''
        self.nOfWC = 0
        self.initialEC = currentgamedeck.initialEC
        self.playingdeck = currentgamedeck.currentECdeck
        self.playerfuncs = playerfuncs
        self.tempfuncs = Funcs(self.PV,self.playerfuncs, 0,0)
        return

    def shuffle(self):
        shuffle(self.playingdeck)
        
    def WCQuantity(self,functionN):
        mycards = dbCards()
        q = mycards.selectWCQuantity(functionN)
        return q

    def updateEC(self, vars,pc,rc):
        self.PV = copy.deepcopy(vars)        
        self.playingdeck = pc
        self.reservedEC = rcf
        return self

    def update_Vars(self,vars):
        self.PV = copy.deepcopy(vars)
        return self

  
    def asignValuetovar(self,var,value):
        if var in self.PV.Nullindex:
            self.PV.Nullindex.remove(var)
        self.PV.varsValue[var]=value        
        return

    def asignVartoVar(self,goalvar,var):
        if goalvar in self.PV.Nullindex:
            self.PV.Nullindex.remove(goalvar)
        if var in self.PV.Nullindex:
            self.PV.Nullindex.append(goalvar)
            self.PV.varsValue[goalvar] = 0
        else:
            self.PV.varsValue[goalvar] = self.PV.varsValue[var]
        return self
            
    def selectNextEC(self):
        self.reset()
        ec = self.playingdeck[0]
        self.currentEC = ec
        self.playingdeck = np.delete(self.playingdeck,[0])
        return self
   
    def reset(self):
        if (len(self.playingdeck) == 0):           
            self.playingdeck = self.initialEC.deck
            self.shuffle()
        return(self)

    def unreserve(self,ec):
        self.reservedEC.discard(ec)
        return

    def selectVar(self):
        vars = copy.deepcopy(self.PV)
        #total should be removed from vars selection
        vars.varsValue = copy.deepcopy(self.PV.varsValue[:3])
        if 3 in vars.Nullindex:
            vars.Nullindex.remove(3)
        if len(vars.Nullindex)>0:     
            #pop remove item and get its value
            r = vars.Nullindex.pop(0)
        else: 
            try:
                r = vars.varsValue.argmin()
            except ValueError:
                r=0
        return r

   #name should change because it check and manage null
    def checknull(self,ind,status,resultvar):
        check = False
        a = any(item in ind for item in self.PV.Nullindex)
        if a == True:
            check = True
        #1. status ==0: only check null A+=8- no special change
        #2. check null to change result but not null of destination(remove null of destination) T= A+B        
        if status == 1:
            if a== True: 
                if not resultvar in self.PV.Nullindex:
                    self.PV.Nullindex.append(resultvar)
                    self.PV.varsValue[resultvar] = 0
            else:#a= false
                if resultvar in self.PV.Nullindex:
                    self.PV.Nullindex.remove(resultvar)
       
        #3. check null for effect of destination T+=A
        if status == 2:
            if check == True and not resultvar  in self.PV.Nullindex:                
                self.PV.Nullindex.append(resultvar)
                self.PV.varsValue[resultvar] = 0
        return (check)
    
    def playFunc(self,s):
        """calling a function with making its name as string"""  
        #self.updateEC(s.P.playerVars, s.EC.playingdeck, s.P.PlayerReservedEC)
        #self.updateEC(s.P.playerVars, s.currentMixedCards, s.P.PlayerReservedEC)
        #self.selectNextEC()
        
        
        FuncName = 'ECFunc' + str(self.currentEC)
        getattr(self, FuncName)()
        self.nOfWC = self.WCQuantity(self.currentEC)
        s.P.updatePlayer(self.PV,0,self.reservedEC,[],self.playerfuncs)    
        #??? deck will update after playing the step?
        #s.GS.currentECdeck = self.playingdeck
        return s

    def updateFunc(self, varnumber, value):
        self.tempfuncs.varnumber = varnumber
        self.tempfuncs.value = value
        return self
    # list of Cards
    #-------------------
    #A: input Cards
    #-------------------
    def ECFunc0(self):
        self.ECName = 'EC:Input:A =3'
        #add insead of asign function
        
        if 3 in self.playerfuncs:
            self.updateFunc(0,3)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(0,3)        
        return(self)

    def ECFunc1(self):
        self.ECName = 'EC:Input:A =7'
        #add insead of asign function
        if 3 in self.playerfuncs:
            self.updateFunc(0,7)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(0,7)
        return(self)
        
    def ECFunc2(self):
        self.ECName = 'EC:Input:A =15'
        #add insead of asign function
        if 3 in self.playerfuncs:
            self.updateFunc(0,15)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(0,15)
        return(self)
      
    def ECFunc3(self):
        self.ECName = 'EC:Input:A =32'
        #add insead of asign function
        if 3 in self.playerfuncs:
            self.updateFunc(0,32)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(0,32)
        return(self)
    
    
    def ECFunc4(self):
        self.ECName = 'EC:Input:A =64'
        #add insead of asign function
        if 3 in self.playerfuncs:
            self.updateFunc(0,64)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(0,64)
        return(self)

    # B input
    
    def ECFunc11(self):
        self.ECName = 'EC:Input:B =8'
        #add insead of asign function
        if 3 in self.playerfuncs:
            self.updateFunc(1,8)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(1,8)
        return(self)

    def ECFunc12(self):
        self.ECName = 'EC:Input:B =16'

        if 3 in self.playerfuncs:
            self.updateFunc(1,16)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(1,16)
        return(self)

    def ECFunc13(self):
        self.ECName = 'EC:Input:B =20'
        if 3 in self.playerfuncs:
            self.updateFunc(1,20)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(1,20)
        return(self)

    def ECFunc14(self):
        self.ECName = 'EC:Input:B =32'
        if 3 in self.playerfuncs:
            self.updateFunc(1,32)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(1,32)
        return(self)

    def ECFunc15(self):
        self.ECName = 'EC:Input:B =64'
        if 3 in self.playerfuncs:
            self.updateFunc(1,64)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(1,64)
        return(self)
    # C Input
    def ECFunc21(self):
        self.ECName = 'EC:Input:C =4'
        if 3 in self.playerfuncs:
            self.updateFunc(2,4)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(2,4)
        return(self)
    # C=15
    def ECFunc22(self):
        self.ECName = 'EC:Input:C = 7'
        if 3 in self.playerfuncs:
            self.updateFunc(2,7)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(2,7)
        return(self)
    # C=25
    def ECFunc23(self):
        self.ECName = 'EC:Input:C =15'
        if 3 in self.playerfuncs:
            self.updateFunc(2,15)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(2,15)
        return(self)
    # C=40
    def ECFunc24(self):
        self.ECName = 'EC:Input:C =40'
        if 3 in self.playerfuncs:
            self.updateFunc(2,40)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(2,40)
        return(self)
    # C=75
    def ECFunc25(self):
        self.ECName = 'EC:Input:C =70'
        if 3 in self.playerfuncs:
            self.updateFunc(2,70)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(2,70)
        return(self)

    def ECFunc31(self):
        self.ECName = 'EC31:Input:T=A'
        if 3 in self.playerfuncs:
            if 0 not in self.PV.Nullindex:
                self.updateFunc(3,self.PV.varsValue[0])
                self.tempfuncs.func3()
                self.PV = self.tempfuncs.PV
        else:
            self.asignVartoVar(3,0)
        return self
   
    def ECFunc32(self):
        self.ECName = 'EC32:T=B' 
        if 3 in self.playerfuncs:
            if 1 not in self.PV.Nullindex:
                self.updateFunc(3,self.PV.varsValue[1])
                self.tempfuncs.func3()
                self.PV = self.tempfuncs.PV
        else:
            self.asignVartoVar(3,1)
        return self
    
    def ECFunc33(self):
        self.ECName = 'EC33:T=C'
        if 3 in self.playerfuncs:
            if 2 not in self.PV.Nullindex:
                self.updateFunc(3,self.PV.varsValue[2])
                self.tempfuncs.func3()
                self.PV =self.tempfuncs.PV
        else:
            self.asignVartoVar(3,2)
        return self

    def ECFunc34(self):
        self.ECName = 'EC34 :T=8'
        if 3 in self.playerfuncs:
            self.updateFunc(3,8)
            self.tempfuncs.func3()
            self.PV = self.tempfuncs.PV
        else:
            self.asignValuetovar(3,8) 
        return self
    #-------------------
    #Task cards functions
    #-------------------
    #-------------------
    #--Task funcitons begin with 100
    #-------------------
    def ECFunc100(self):
        self.ECName = 'EC100:Task:T+=A'
        ind = [0]
        indif = [0]
        if not self.checknull(indif,2,3):
             self.PV.varsValue[3]=np.sum(self.PV.varsValue[ind])+(self.PV.varsValue[3])
        return self
   
    def ECFunc101(self):
        self.ECName = 'EC101:Task:T+=B'
        ind = [1]
        indif = [1]
        if not self.checknull(indif,2,3):
             self.PV.varsValue[3]=np.sum(self.PV.varsValue[ind])+(self.PV.varsValue[3])
        return self
    
    def ECFunc102(self):
        self.ECName = 'EC102:Task:T+=C'
        ind = [2]
        indif = [2]
        if not self.checknull(indif,2,3):
             self.PV.varsValue[3]=np.sum(self.PV.varsValue[ind])+(self.PV.varsValue[3])
        return self

    def ECFunc103(self):
        self.ECName = 'EC102:Task:T+=8'
        indif = [3]
        if not self.checknull(indif,0,3):
             self.PV.varsValue[3]= 8 +(self.PV.varsValue[3])
        return self

    def ECFunc104(self):
        self.ECName = 'EC:Task: T += A+B'
        ind= [0,1]
        if not self.checknull(ind,2,3):
                #all are not null and possible to add
                ind = [0,1,3]
                self.PV.varsValue[3] = np.sum(self.PV.varsValue[ind])
        return(self)


    def ECFunc105(self):
        self.ECName = 'EC:Task: T += A+B+C' 
        ind =[0,1,2]   
        if not self.checknull(ind,2,3):
            self.PV.varsValue[3] = sum(self.PV.varsValue)
        return(self)
 
    def ECFunc106(self):
        self.ECName = 'EC:Task: T += sum all'
        ind =[0,1,2]
        if not self.checknull(ind,2,3):
            self.PV.varsValue[3] = np.sum(self.PV.varsValue)
        return(self)
   
    def ECFunc107(self):
        self.ECName = 'EC:Task: x += 8 ! total'        
        if not self.checknull([0],0,-1):
            self.PV.varsValue[0] = (self.PV.varsValue[0]) + 8
        
        if not self.checknull([1],0,-1):
            self.PV.varsValue[1] = (self.PV.varsValue[1]) + 8
        
        if not self.checknull([2],0,-1):
            self.PV.varsValue[2] = (self.PV.varsValue[2]) + 8
        return self



    def ECFunc112(self):
        self.ECName = 'aEC:Task: T = A+B'
        ind = [0,1]
        indif= [0,1]
        if not self.checknull(indif,1,3):
                self.PV.varsValue[3] = np.sum(self.PV.varsValue[ind])
        return(self)
    #-------------------
    #resource functions
    #-------------------
    def ECFunc200(self):
        self.ECName = 'EC:Resource: Restart'
        self.reservedEC.append(200)
        return(self)
    #-------------------
    #player functions
    #0: zero instead of null
    #1: absolute value
    #2: add instead of reduce
    #3: add instead of assign
    #-------------------
    def ECFunc201(self):
        self.ECName = 'EC:Resource: Freelancer'
        #tempfunc = Funcs(self.PV,self.playerfuncs,0,0)
        x = self.tempfuncs.buyFunc()
        if x == False:
            self.reservedEC.append(201)                        
        return(self)

    def ECFunc202(self):
        self.ECName = 'EC:Resource: Bazar'
        self.reservedEC.append(202)
        return(self)