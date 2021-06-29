from enum import Enum
class GameSettings():
    sampleQuantity = 100
    winGoal = 100
    #it should be one more of last function number because the functions name are begining with number 0
    #NrofEC = 32
    #NrOfWC = 15
    NrOfP = 2
    maxRound = 40
    Testchangelog ="lego: wc chalange 1 to 5"
   #"only EC-q=[1,4,3,2]-adding new task[103]"

    EC_Types = "Luck,Normal,Week"
    EC_Luck         =   [28,24,7,18]
    EC_Normal       =   [5,10,35,37,36,16,6,11,17,12]
    EC_NormalTask   =   [100,101,102,103,514,515,516]
    EC_Week         =   [4,15,34]
    EC_Resource     =   [200,201,202]
    #EC_BigLuck =[21,8,14,19,25,27,20,26,22]
    


    WC_Types = "Bad luck, normal, week"
    WC_BigBadLuck    =  [6]
    WC_BadLuck       =  [5,4]
    WC_Week          =  [12,13,14]
    WC_Challange     =  [0,1,2,3,7,10,11]
    WC_Normal        =  [8,9,15]
    WC_Cards         =  [WC_Week, WC_Normal, WC_Challange, WC_BadLuck]
   
    # sum quantity should reach Steps number (40 max round * 2 player=80), it is still less because some cards have 2 worms
    WC_Quantity      = [5,5,5,2] 
    #[20,10,1,1]
    #[5,5,1] without lego
#---------------------
#lego
#------------------------
    EC_lego_Luck         =   [25,517]
    EC_lego_Normal       =   [502,503,506,507,510,511]
    EC_lego_NormalTask   =   [20,21,22,100,101,102,103]
    EC_lego_Week         =   [500,501,504,505,508,509, 512]
    EC_lego_Resource     =   [29,30,31]
#--------------------------------------------------------------
    #EC_Cards        =   [EC_Luck,EC_Normal,EC_NormalTask,EC_Week]
    EC_Cards        =   [EC_lego_Luck,EC_lego_Normal,EC_lego_NormalTask,EC_lego_Week,EC_lego_Resource]
    EC_Quantity     =   [2,5,5,5,4] #[3,30,30,5,2]    
#----------------------------
    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']
    ResourceEC         =   {'EC31:Resource: Bazar','EC30:Resource: Freelancer','EC29:Resource: Restart'
                   }


    

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
        
