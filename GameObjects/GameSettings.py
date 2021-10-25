from enum import Enum

class GameSettings():





    WC_BadLuck       =  [6,5,4]
    WC_Week          =  [12,13,14]
    WC_Challange     =  [0,1,2,3,7,10,11]
    WC_Normal        =  [8,9,15]
#------------------------
#lego
#------------------------
    EC_lego_Luck     =  [4,15,25]
    EC_lego_Luck_task = [104,105,106]
    EC_lego_Normal       =   [2,3,12,13,14,23,24]
    EC_lego_NormalTask   =   [100,101,102,103,107,112]
    EC_ChalangeInput      =   [31,32,33,34]
    EC_lego_Week         =   [0,1,11,21,22]
    EC_lego_Resource     =   [200,201,202]

#-----------------
    sampleQuantity = 100
    winGoal = 128
    #it should be one more of last function number because the functions name are begining with number 0
    NrOfP = 2
    maxRound = 40
    Testchangelog =" only EC : week 0 -> 1  "
#--------------------------------------------------------------
    EC_Cards        =   [EC_lego_Luck_task,EC_lego_Luck,EC_lego_Normal,EC_lego_NormalTask,EC_ChalangeInput,EC_lego_Week,EC_lego_Resource]
    EC_Quantity     =   [0,0,2,3,0,1,0] 
#----------------------------
    WC_Cards         =  [WC_Week, WC_Normal, WC_Challange, WC_BadLuck]   
    WC_Quantity      = [10,1,1,1] 

# sum quantity should reach Steps number (40 max round * 2 player=80), it is still less because some cards have 2 worms







    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']
    ResourceEC         =   {'EC31:Resource: Bazar','EC30:Resource: Freelancer','EC29:Resource: Restart' }


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
