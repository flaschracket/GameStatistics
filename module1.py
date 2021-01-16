from GameObjects.Player import Player
from GameObjects.EventCards import *
from random import randrange



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
#    print('function is:'+str(choosingEC))
    CallECFunc(choosingEC)
    self.sumplayedEC = self.sumplayedEC + 1
 #   print('sumplaidfuncs=' + str(sumplayedEC))
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
    