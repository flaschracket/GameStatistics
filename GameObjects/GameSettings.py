from enum import Enum
class GameSettings():
    sampleQuantity = 100
    winGoal = 100
    #it should be one more of last function number because the functions name are begining with number 0
    #NrofEC = 32
    #NrOfWC = 15
    NrOfP = 2
    maxRound = 40
    #pauseplayingcount = 2

    Testchangelog = "only EC-q=[2,5,5]"
    EC_Types = "Luck,Normal,Week"
    EC_Quantity    = [2,5,5]
    WC_Types = "No WC"
    WC_Quantity      = [1,10,20]

    EC_Luck =   [25,21,22,28,24]
    EC_BigLuck =[27,20,26]
    EC_Normal = [0,1,2,7,8,13,14,19,23]
    EC_Week =   [3,4,5,6,9,10,11,12,15,16,17,18]
    EC_Resource = [29,30,31]
    
    WC_BadLuck       =  [5]
    WC_Week          =  [12,13,14]
    WC_Normal        =  [0,1,2,3,4,6,7,8,9,10,11]


    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']

    ChanceEC = {'EC25(2w):Task: T += sum all','EC22:Task: T += A+B+C'  , 'EC21:Task: T += A+B', 'EC24(2w):Task: T += sum all/2','EC28(2w):Task: x = 2x ! total' }
    Bigluck = {'EC27(2w):Task: T += (2*)(A+B+C)','EC20:Task: T = A*B','EC26(2w):Task: T += B+((2*)A)'}
    weakEC = {  'EC3:Input:2 digit number<30',    'EC4:Input:A =5',    'EC5:Input:A =10',    'EC6:Input:A =25', 
                'EC9:Input: sum dice of all players', 'EC10:Input:B =10', 'EC11:Input:B =20',     'EC12:Input:B =30',
                'EC15:Input:C =5',    'EC16:Input:C =15',    'EC17:Input:C =25','EC18:Input:C =45'}
    
    NormalEC = {'EC0: Input:2 digit number', 'EC1:Input:2 digit number<50','EC2:Input:2 digit number<90', 'EC7:Input:A =50',
               'EC8:Input:A =75','EC13:Input:B =50','EC14:Input:B =70', 'EC19:Input:C =75','EC31:Resource: Bazar',
               'EC30:Resource: Freelancer','EC29:Resource: Restart',
               'EC23:Task: T = xx9x'}


    WCNames ={' WC0: A=NULL; ',' WC1: B=NULL; ',' WC2: C=NULL; ',' WC3: B,C=0; ',' WC4: T -=100 ',' WC5: Capture CPU ',
              ' WC6: T =xx00 ',' WC7: A=0,B=-1,C=N ',' WC8: B=-10 ',' WC9: C=-20 ',' WC10: A=0 ',' WC11: B=0 ',' WC12: B+=-10 ',' WC13: A+=-10 ',' WC14: C+=-10 '}


    def _init_(self):
      ECCollection2 =  dict()
      self.initial_cards(1,10,3)
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
        
