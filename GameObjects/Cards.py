from random import shuffle
import numpy as np
class Cards():
    """description of class"""


    def __init__(self,*args,**kwargs):
        
            values = [1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13]
            quantites = 3
            self.deck = []
            self.mycards = kwargs.get('quantity',values)
            self.suites = kwargs.get('cardsVaraity',quantites)
            self.deck = np.repeat(self.mycards,quantites)
            return

    def shuffle(self):
         shuffle(self.deck)

    def deal(self, n_players):
            self.hands = [self.deck[i::n_players] for i in range(0, n_players)]
