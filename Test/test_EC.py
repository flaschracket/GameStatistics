#import pyodbc
import numpy as np
import unittest
from GameObjects.EventCards import EventCards
from GameObjects.MainRAMVars import MainRAMVars
from GameObjects.GameDeck import GameDeck
#>python3 -m unittest Test.test_EC
class Test_test_EC(unittest.TestCase):
    #func 112
    def test_ECFunc112_A(self):
        Aev = EventCards(MainRAMVars(),[],GameDeck(),[])      
        Aev.playerFuncs = [4]
        Aev.PV.varsValue =np.array([1,2,0,1])
        Aev.ECFunc112()
        result = Aev.PV.varsValue[3]
        self.assertEqual(result,4)
    #func 201
    # test if add the card to array
    def test_ECFunc201_A0(self):
        Bev = EventCards(MainRAMVars(),[],GameDeck(),[])
        Bev.PV.varsValue =np.array([10,10,10,1])
        Bev.ECFunc201()
        Bresult = len(Bev.reservedEC)
        self.assertEqual(Bresult,1)        

    def test_ECFunc201_A2(self):
        Cev = EventCards(MainRAMVars(),[201],GameDeck(),[])
        Cev.PV.varsValue =np.array([-6,0,40,0])
        Cev.ECFunc201()
        Cresult = len(Cev.reservedEC)
        self.assertEqual(Cresult,2)        

    def test_ECFunc201_A3(self):
        Cev = EventCards(MainRAMVars(),[201,201],GameDeck(),[])
        Cev.PV.varsValue =np.array([-6,0,40,0])
        Cev.ECFunc201()
        Cresult = len(Cev.reservedEC)
        self.assertEqual(Cresult,3)        

if __name__ == '__main__':
    unittest.main()
