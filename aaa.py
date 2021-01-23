from GameObjects.Player import Player
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from GameObjects.Step import *
from random import randrange


#Game Setup information
EC = EventCards()
WC = WormCards()
S = Step()

corruption = 0
sumplayedEC = 0
#playedCardsSet = {0}
def initialgame():
        #get the players
    self.nofPlayers = int(input("how many players are playing the game?"))
        #for x in range(self.nofPlayers):
         #   self.currentPlayer.Name = input("what is the name of Player" + str(x+1) + " : ")        
 #           self.listofPlayers.append(self.currentPlayer)
    return True
def CallECFunc(ECNummber,Player):
    """calling a function with making its name as string"""
    FuncName = 'ECFunc'+ str(ECNummber)
    funcresult = getattr(EC, FuncName)()
    return(funcresult)

def CallWCFunc(WCnumber, Player):
    """calling a function with making its name as string"""
    FuncName = 'WCFunc'+ str(WCnumber)
    funcresult = getattr(WC , FuncName)()
    return funcresult

   

def GoForward(self,whosTurn):
    myturn =self.mygame.listofPlayers[whosTurn]
    S.currentStep = S.currentStep+1
    choosingEC = SelectEC(self)
    nOfCorruption = CallECFunc(choosingEC,myturn)
    #print('number of corruption: '+ str(nOfCorruption))
    self.sumplayedEC = self.sumplayedEC + 1
    OMGCorruption(self,myturn)   
    if (self.sumplayedEC == EC.totalEventCards):
     #   print('All EC Cards are played')
        self.sumplayedEC = 0
        playedCardsSet.clear()

def OMGCorruption(self, p=Player()):
    SelectedWC = 1
    self.CallWCFunc(SelectedWC, p)    

