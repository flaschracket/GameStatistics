from enum import Enum
from DB.dbCards import *

class GameSettings():
    WC_BadLuck       =  [6,5,4]
    WC_Week          =  [12,13,14]
    WC_Challange     =  [0,1,2,3,7,10,11]
    WC_Normal        =  [8,9,15]
#------------------------
#lego
#------------------------
#-----------------
    sampleQuantity = 100
    winGoal = 128
#it should be one more of last function number because the functions name are begining with number 0
    NrOfP = 2
    maxRound = 120
    Testchangelog = "only one chalange -1:2"
#----------------------------
    WC_Cards        =  [WC_Week, WC_Normal, WC_Challange, WC_BadLuck]   
    WC_Quantity     =  [10,1,1,1] 
# sum quantity should reach Steps number (40 max round * 2 player=80), it is still less because some cards have 2 worms

    resourceECtypes = ['Restart','Bazar','Freelancer']
    PCstatus = ['shutdown', 'CPU1Captured', '']
    ResourceEC         =   {'EC31:Resource: Bazar','EC30:Resource: Freelancer','EC29:Resource: Restart' }

#---------------------------
    def __init__(self):
        mycards = dbCards()
        self.EC_Cards = []
        self.cardsCategory = mycards.selectAllCategoryID()
        for i in self.cardsCategory:
            newlist = mycards.selectCardsofCategory(i)
            self.EC_Cards.append(newlist)
        self.EC_Quantity = mycards.selectAllCategoryQuantity()
        return


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
