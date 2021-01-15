from GameObjects.Player import Player
from GameObjects.EventCards import *
from random import randrange

firstplayer = Player()
GameStep = 0
PlayedCards= ''
EC = EventCards()

def SelectEC(self):
    choosingEC= 0
    choosingEC = randrange(10)
    self.PlayedCards= PlayedCards+','+str(choosingEC)
    return choosingEC
def TestPrint():
    print("Hello From Module")          
    print("list(DefinedEnums.EventCardType)  has error to print")
    firstplayer._init_()
    firstplayer.printstatus()

def GoForward(self):
    self.GameStep = self.GameStep+1
    choosingEC=SelectEC(self)
    CallECFunc(choosingEC)

def CallECFunc(EventCardNummber):
    print('Hello from call funtion')
    
    """calling a function with making its name as string"""
    FuncName = 'ECFunc'+ str(EventCardNummber)
    funcresult = getattr(EC, FuncName)()
    print('Random function is called:')
    print(funcresult)
    