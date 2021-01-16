from GameObjects.Player import Player
from GameObjects.EventCards import *
from random import randrange


#Game Setup information
numberofPlayers = 0
listofPlayers = []
#allPlaylers[10] = Player()
CurrentStep = 0
sumplayedEC = 0
playedCardsSet = {0}

firstplayer = Player()
EC = EventCards()

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

def GoForward(self):
    self.CurrentStep = self.CurrentStep+1
    choosingEC = SelectEC(self)
    CallECFunc(choosingEC)
    self.sumplayedEC = self.sumplayedEC + 1
    if (self.sumplayedEC == EC.totalEventCards):
        print('All EC Cards are played')
        playedCardsSet.clear()

def CallECFunc(EventCardNummber):
  #  print('Hello from call funtion')
    """calling a function with making its name as string"""
    FuncName = 'ECFunc'+ str(EventCardNummber)
    funcresult = getattr(EC, FuncName)()
   # print('Random function is called:')
   # print(funcresult)
    

def Gamesetup(self):
    numberofPlayers = int(input("how many players are playing the game?"))
    ply = Player()
    for x in range(numberofPlayers):
        ply.Name = input("what is the name of Player" + str(x+1) + " : ")        
        listofPlayers.append(ply)
        listofPlayers[x].printstatus()