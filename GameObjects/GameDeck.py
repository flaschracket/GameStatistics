from DB.dbCards import *
from GameObjects.Cards import *


class GameDeck(object):
    """description of class"""
    def __init__(self):
        #---------------EC-------------
        #gathering EC card info from DB
        # sum quantity should reach Steps number (40 max round * 2 player=80), it is still less because some cards have 2 worms
        mycards = dbCards()
        dbcon = database().connectdb()
        self.EC_Cards = []
        self.cardsCategory = mycards.selectAllCategoryID(1,dbcon)
        for i in self.cardsCategory:
            newlist = mycards.selectCardsofCategory(i,1)
            self.EC_Cards.append(newlist)
        self.EC_Quantity = mycards.selectAllCategoryQuantity(1)
        
        #making list of EC from data selected from DB
        cards  = self.EC_Cards
        q    = self.EC_Quantity
        ecs = Cards(cardsVaraity = cards, quantities =  q )
        self.initialEC = copy.deepcopy(ecs)
        self.initialEC.shuffle()
        self.currentECdeck = self.initialEC.deck
        #------------WC-------------
        #gathering WC card info from DB
        wccards = dbCards()
        WC_Cards = []
        self.WCcardsCategory = wccards.selectAllCategoryID(2,dbcon)
        for i in self.WCcardsCategory:
            newlist = mycards.selectCardsofCategory(i,2)
            WC_Cards.append(newlist)
        self.WC_Quantity = wccards.selectAllCategoryQuantity(2)
        #making list of WC
        self.initialWC = Cards(cardsVaraity = WC_Cards, quantities =  self.WC_Quantity )
        self.initialWC.shuffle()
        self.currentWCdeck = self.initialWC.deck

        #--------------mixed Deck-----------------
        
        MixedCardsQuantities = self.EC_Quantity
        for i in self.WC_Quantity:
            MixedCardsQuantities.append(i)

        MixedCardsVaraity = self.EC_Cards
        for j in WC_Cards:
            newlist = []
            for i in j:
                k = 5000+i
                newlist.append(k)
            MixedCardsVaraity.append(newlist)

        self.initialMixedCards = Cards(cardsVaraity = MixedCardsVaraity, quantities = MixedCardsQuantities)    
        self.initialMixedCards.shuffle()
        self.currentMixedCards = self.initialMixedCards.deck
        return


