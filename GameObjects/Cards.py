from random import shuffle
import numpy as np
class Cards():
    """description of class"""


    def __init__(self,*args,**kwargs):
        
            values = np.array([1 , 2 ])
            quantites = np.array([3 , 2])
            self.deck = np.array([1])
            
            self.mycards = kwargs.get('quantity',values)
            self.quantites = kwargs.get('cardsVaraity',quantites)
            
            for i in range(len(self.quantites)):
                 cardsdeck = np.repeat(self.mycards[i],self.quantites[i])
                 self.deck = np.append(self.deck,cardsdeck)
                 #np.append(self.deck,cardsdeck)
                 #print("initial")
                 #print(self.deck)
            return

    def shuffle(self):
         shuffle(self.deck)

    def deal(self, n_players):
            self.hands = [self.deck[i::n_players] for i in range(0, n_players)]
