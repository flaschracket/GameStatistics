from enum import Enum
class GameSettings():
    sampleDataNumber = 100
    winGoal = 100
    #it should be one more of last function number because the functions name are begining with number 0
    NrofEC = 32
    NrOfWC = 15
    NrOfP = 2
    StoponThisRound = 40
    pauseplayingcount = 2

    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']

    ChanceEC = {'EC27(2w):Task: T += (2*)(A+B+C)','EC20:Task: T = A*B','EC26(2w):Task: T += B+((2*)A)','EC25(2w):Task: T += sum all'}

    weakEC = {  'EC3:Input:2 digit number<30',    'EC4:Input:A =5',    'EC5:Input:A =10',    'EC6:Input:A =25', 
                'EC9:Input: sum dice of all players', 'EC10:Input:B =10', 'EC11:Input:B =20',     'EC12:Input:B =30',
                'EC15:Input:C =5',    'EC16:Input:C =15',    'EC17:Input:C =25','EC18:Input:C =45'}
    
    NormalEC = {'EC0: Input:2 digit number', 'EC1:Input:2 digit number<50','EC2:Input:2 digit number<90', 'EC7:Input:A =50',
               'EC8:Input:A =75','EC13:Input:B =50','EC14:Input:B =70', 'EC19:Input:C =75','EC31:Resource: Bazar',
               'EC30:Resource: Freelancer','EC29:Resource: Restart','EC28(2w):Task: x = 2x ! total', 'EC24(2w):Task: T += sum all/2' ,
               'EC23:Task: T = xx9x','EC22:Task: T += A+B+C'  , 'EC21:Task: T += A+B'}

    ChanceECcoll = dict({27:0,20:0,25:0,26:0,21:1,22:1})
    WeakECcoll   = dict({3:20,4:20,5:20,6:20,9:20,10:20,11:20,12:20,15:20,16:20,17:20,18:20})
    NormalECcoll = dict({0:30,1:30,2:30,7:30,8:30,13:30,14:30,19:30,23:30,29:0,30:0,31:0})
    Normal2WC    = dict({28:1,24:1})
    ECCollection = dict({**ChanceECcoll , **WeakECcoll, **NormalECcoll, **Normal2WC})

    ECPlayedCollection = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0}
    WCNames ={' WC0: A=NULL; ',' WC1: B=NULL; ',' WC2: C=NULL; ',' WC3: B,C=0; ',' WC4: T -=100 ',' WC5: Capture CPU ',
              ' WC6: T =xx00 ',' WC7: A=0,B=-1,C=N ',' WC8: B=-10 ',' WC9: C=-20 ',' WC10: A=0 ',' WC11: B=0 ',' WC12: B+=-10 ',' WC13: A+=-10 ',' WC14: C+=-10 '}
    
    BadluckWC       =  dict({5:6})
    weekWC          =  dict({12:60,13:60,14:60})
    NormalWC        =  dict({0:20,1:20,2:20,3:20,4:20,6:20,7:20,8:20,9:20,10:20,11:20})
    WCCollection    =  dict({**weekWC, **NormalWC, **BadluckWC})
    WCPlayedCollection = {0:0,1:10,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}


    def _init_(self):
        return self    
#------------------
#----------------
    def ifWined(self,total):
        wined= False
        if (total >= self.winGoal):
            wined = True
        return wined

    class GameHardware(Enum): 
        MainRAM = 0
        ExtraRAM = 1
        CPU1 = 2
        CPU2 = 3
        SSD = 4

    @property
    def primary_PC(self):
        return self.MainRAM, self.CPU1
    
    class ResourceECTypes(Enum): 
        Restart = 0
        Bazar = 1
        Freelancer = 2
        
