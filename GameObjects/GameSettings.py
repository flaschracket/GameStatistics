from enum import Enum
from DB.dbCards import *
from GameObjects.Cards import *

class GameSettings():
#-----------------
#    PCstatus = ['shutdown', 'CPU1Captured', '']
#    ResourceEC         =   {'EC31:Resource: Bazar','EC30:Resource: Freelancer','EC29:Resource: Restart' }
# self.resourceECtypes =  ['Restart','Bazar','Freelancer']

#---------------------------
    def __init__(self):
        #---------------EC-------------
        #gathering EC card info from DB
        # sum quantity should reach Steps number (40 max round * 2 player=80), it is still less because some cards have 2 worms
#        mycards = dbCards()
 #       dbcon = database().connectdb()
  #      self.EC_Cards = []
   #     self.cardsCategory = mycards.selectAllCategoryID(1,dbcon)
    #    for i in self.cardsCategory:
     #       newlist = mycards.selectCardsofCategory(i,1)
      #      self.EC_Cards.append(newlist)
       # self.EC_Quantity = mycards.selectAllCategoryQuantity(1)
        
        #making list of EC from data selected from DB
#        cards  = self.EC_Cards
 #       q    = self.EC_Quantity
  #      ecs = Cards(cardsVaraity = cards, quantities =  q )
   #     self.initialEC = copy.deepcopy(ecs)
    #    self.initialEC.shuffle()
     #   self.currentECdeck = self.initialEC.deck
        #------------WC-------------
        #gathering WC card info from DB
#        wccards = dbCards()
 #       self.WC_Cards = []
  #      self.WCcardsCategory = wccards.selectAllCategoryID(2,dbcon)
   #     for i in self.WCcardsCategory:
    #        newlist = mycards.selectCardsofCategory(i,2)
     #       self.WC_Cards.append(newlist)
     #   self.WC_Quantity = wccards.selectAllCategoryQuantity(2)
        #making list of WC
#        self.initialWC = Cards(cardsVaraity = self.WC_Cards, quantities =  self.WC_Quantity )
 #       self.initialWC.shuffle()
  #      self.currentWCdeck = self.initialWC.deck
        #-others
        self.gsID = 0
        self.restart = 200
        self.sampleQuantity = 5
        self.winGoal = 128
        self.NrOfP = 2
        self.maxRound = 40
        self.Testchangelog = "test logic of program after changings"
        return

    def ifWined(self,total):
         wined= False
         if (total >= self.winGoal):
                wined = True
         return wined
    
    
    #class GameHardware(Enum): 
    #    MainRAM = 0
   #     ExtraRAM = 1
  #      CPU1 = 2
 #       CPU2 = 3
#        SSD = 4

#    @property
#    def primary_PC(self):
#         return self.MainRAM, self.CPU1

#use in rules
    class ResourceECTypes(Enum): 
           Restart = 0
           Bazar = 1
           Freelancer = 2
