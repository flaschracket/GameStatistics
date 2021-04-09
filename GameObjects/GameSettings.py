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

    ChanceEC = {'EC27:Task: T += (2*)(A+B+C)','EC20:Task: T = A(*)+B','EC26:Task: T += B+((2*)A)','EC25:Task: T += sum all'}

    weakEC = {  'EC3:Input:2 digit number<30',    'EC4:Input:A =5',    'EC5:Input:A =10',    'EC6:Input:A =25', 
                'EC9:Input: sum dice of all players', 'EC10:Input:B =10', 'EC11:Input:B =20',     'EC12:Input:B =30',
                'EC15:Input:C =5',    'EC16:Input:C =15',    'EC17:Input:C =25','EC18:Input:C =45'}
    
    NormalEC = {'EC0: Input:2 digit number', 'EC1:Input:2 digit number<50','EC2:Input:2 digit number<90', 'EC7:Input:A =50',
               'EC8:Input:A =75','EC13:Input:B =50','EC14:Input:B =70', 'EC19:Input:C =75','EC31:Resource: Bazar',
               'EC30:Resource: Freelancer','EC29:Resource: Restart','EC28:Task: x = 2x ! total', 'EC24:Task: T += sum all/2' ,
               'EC23:Task: T = xx9x','EC22:Task: T += A+B+C'  , 'EC21:Task: T += A+B'}

    ChanceECcoll =dict({27:3,20:3,25:3,26:3})
    WeakECcoll   = dict({3:10,4:9,5:9,6:10,9:10,10:9,11:10,12:9,15:10,16:9,17:10,18:9})
    NormalECcoll  =dict({0:80,1:40,2:80,7:60,8:80,13:60,14:80,19:80,21:60,22:40,23:30,24:60,28:80,29:60,30:40,31:80})
    ECCollection =dict({**ChanceECcoll , **WeakECcoll, **NormalECcoll})

    ECPlayedCollection = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0}
    WCNames ={' WC0: A=NULL; ',' WC1: B=NULL; ',' WC2: C=NULL; ',' WC3: B,C=0; ',' WC4: T -=100 ',' WC5: Capture CPU ',
              ' WC6: T =xx00 ',' WC7: A=0,B=-1,C=N ',' WC8: B=-10 ',' WC9: C=-20 ',' WC10: A=0 ',' WC11: B=0 ',' WC12: B+=-10 ',' WC13: A+=-10 ',' WC14: C+=-10 '}
    WCCollection       = {0:10,1:10,2:10,3:40,4:1,5:3,6:2,7:10,8:20,9:10,10:40,11:40,12:40,13:40,14:40}
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
        
