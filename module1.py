from GameObjects.Player import Player
from GameObjects.EventCards import *
from GameObjects.WormCards import *
from GameObjects.Game import *
from GameObjects.Step import *
from random import randrange


#Game Setup information
EC = EventCards()
WC = WormCards()
G = Game()
S = Step()

corruption = 0
sumplayedEC = 0
playedCardsSet = {0}


def Gamesetup(self):
    numberofPlayers = int(input("how many players are playing the game?"))
    ply = Player()
    for x in range(numberofPlayers):
        ply.Name = input("what is the name of Player" + str(x+1) + " : ")        
        self.G.listofPlayers.append(ply)

def SelectEC(self):
    choosingEC= 0
    while choosingEC in playedCardsSet:
        choosingEC = randrange(11)
        
    playedCardsSet.add(choosingEC)
    print(playedCardsSet)
    return choosingEC

def TestPrint():
    print("Hello From Module")          
    firstplayer._init_()
    firstplayer.printstatus()
    self.G.listofPlayers[1].printstatus()


def CallECFunc(ECNummber,Player):
    """calling a function with making its name as string"""
    FuncName = 'ECFunc'+ str(ECNummber)
    funcresult = getattr(EC, FuncName)()
    return(funcresult)

def CallWCFunc(WCnumber, Player):
    """calling a function with making its name as string"""
    FuncName = 'WCFunc'+ str(WCnumber)
    funcresult = getattr(WC , FuncName)()


   

def GoForward(self,whosTurn):
    myturn =self.G.listofPlayers[whosTurn]
    S.currentStep = S.currentStep+1
    choosingEC = SelectEC(self)
    nOfCorruption = CallECFunc(choosingEC,myturn)
    print('number of corruption: '+ str(nOfCorruption))
    self.sumplayedEC = self.sumplayedEC + 1
   
    OMGCorruption(self,myturn)
   
    if (self.sumplayedEC == EC.totalEventCards):
        print('All EC Cards are played')
        self.sumplayedEC = 0
        playedCardsSet.clear()

def OMGCorruption(self, p=Player()):
    SelectedWC = 1
    self.CallWCFunc(SelectedWC, p)    

def playARound(self):
    for x in range(len(self.G.listofPlayers)):
        GoForward(self,x)
        self.G.Winer = self.G.WhoIsWinner()
        if (self.G.Winer != ''):
             break

