from random import shuffle
import numpy as np
class Cards():
    """description of class"""


    def __init__(self,*args,**kwargs):
        mycards = np.array([]).astype(int)
        quantity = np.array([]).astype(int)
        self.deck = np.array([]).astype(int)   
        self.quantites = np.array([]).astype(int)
        self.mycards   = np.array([]).astype(int)        
        self.mycards = kwargs.get('cardsVaraity', mycards)
        self.quantites = kwargs.get('quantities', quantity)
        self.makelistofcards()
      
        return
    
    def makelistofcards(self):
        for i in range(len(self.quantites)):
            cardsdeck = np.repeat(self.mycards[i],self.quantites[i])
            self.deck = np.append(self.deck,cardsdeck)
        return

    def shuffle(self):
         shuffle(self.deck)

    def deal(self, n_players):
            self.hands = [self.deck[i::n_players] for i in range(0, n_players)]
