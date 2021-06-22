from enum import Enum
class GameSettings():
    sampleQuantity = 100
    winGoal = 100
    #it should be one more of last function number because the functions name are begining with number 0
    #NrofEC = 32
    #NrOfWC = 15
    NrOfP = 2
    maxRound = 40
    Testchangelog ="Test the cards with lego- move WC4 to badluck"
   #"only EC-q=[1,4,3,2]-adding new task[103]"
    EC_Types = "Luck,Normal,Week"
    EC_Luck         =   [28,24,7,18]
    EC_Normal       =   [5,10,35,37,36,16,6,11,17,12]
    EC_NormalTask   =   [100,101,102,103]
    EC_Week         =   [4,15,34]
    EC_Resource     =   [200,201,202]
    #EC_BigLuck =[21,8,14,19,25,27,20,26,22]
    


    WC_Types = "Bad luck, normal, week"
    WC_BigBadLuck    =  [6]
    WC_BadLuck       =  [5,4]
    WC_Week          =  [12,13,14]
    WC_Normal        =  [0,1,2,3,7,8,9,10,11]    
    WC_Cards         =  [WC_Normal, WC_Week, WC_BadLuck]
    WC_Quantity      =  [5,15,1]
#---------------------
#lego
#------------------------
    EC_lego_Luck         =   [24, 512]
    EC_lego_Normal       =   [502,503,506,507,510,511]
    EC_lego_NormalTask   =   [100,101,102,103]
    EC_lego_Week         =   [500,501,504,505,508,509]
    EC_lego_Resource     =   [29,30,31]
#--------------------------------------------------------------
    #EC_Cards        =   [EC_Luck,EC_Normal,EC_NormalTask,EC_Week]
    EC_Cards        =   [EC_lego_Luck,EC_lego_Normal,EC_lego_NormalTask,EC_lego_Week]
    EC_Quantity     =   [1,3,3,2]    
#----------------------------
    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']
    ChanceEC = {'EC21:Task: T += A+B','EC28(2w):Task: x = x+10 ! total','EC24(2w):Task: T += sum all/2','EC7:Input:A =40',
                    'EC18:Input:C =40'}
        #'EC13:Input:B =45',
    Bigluck = {'EC25(2w):Task: T += sum all','EC22:Task: T += A+B+C' , 'EC27(2w):Task: T += (2*)(A+B+C)',
                   'EC20:Task: T = A*B','EC26(2w):Task: T += B+((2*)A)','EC8:Input:A =75','EC14:Input:B =70', 'EC19:Input:C =75'}

    weakEC = { 'EC4:Input:A =5','EC34:Input:B =5','EC15:Input:C =5',
    #              'EC4:Input:A =1','EC34:Input:B =1','EC15:Input:C =1',                       
                  } 
        #'EC23:Task: T = xx9', it work not correctly
    NormalTasskEC ={'EC100:Task:T+=A','EC101:Task:T+=B','EC102:Task:T+=C','EC103:Task:T+=10'}
    NormalEC = { 'EC5:Input:A =10','EC10:Input:B =10','EC35:Input:C =10',
                     'EC36:Input:A =15', 'EC37:Input:B =15','EC16:Input:C =15',
                     'EC6:Input:A =25','EC11:Input:B =25', 'EC17:Input:C =25',
                     'EC12:Input:B =30',
                   }
    ResourceEC         =   {'EC31:Resource: Bazar','EC30:Resource: Freelancer','EC29:Resource: Restart'
                   }

    RandomEC  = {'EC3:Input:2 digit number<30','EC9:Input: sum dice of all players','EC0: Input:2 digit number','EC1:Input:2 digit number<50','EC2:Input:2 digit number<90'}

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
        
