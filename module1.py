from GameObjects.Player import Player
from GameObjects.EventCards import *
from random import randrange



CurrentStep = 0
sumplayedEC = 0
PlayedCardsSet = {0}

firstplayer = Player()
EC = EventCards()

def SelectEC(self):
    choosingEC= 0
    while choosingEC in PlayedCardsSet:
        choosingEC = randrange(10)
        """        self.PlayedCards= PlayedCards+','+str(choosingEC)"""
    PlayedCardsSet.add(choosingEC)
    return choosingEC

def TestPrint():
    print("Hello From Module")          
    print("list(DefinedEnums.EventCardType)  has error to print")
    firstplayer._init_()
    firstplayer.printstatus()

def GoForward(self):
    self.CurrentStep = self.CurrentStep+1
    choosingEC = SelectEC(self)
    CallECFunc(choosingEC)
    self.sumplayedEC = self.sumplayedEC + 1
    if (self.sumplayedEC == EC.totalEventCards):
        PlayedCardsSet = {}

def CallECFunc(EventCardNummber):
    print('Hello from call funtion')
    """calling a function with making its name as string"""
    FuncName = 'ECFunc'+ str(EventCardNummber)
    funcresult = getattr(EC, FuncName)()
    print('Random function is called:')
    print(funcresult)
    