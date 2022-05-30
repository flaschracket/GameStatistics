#import pyodbc
import numpy as np
import unittest
from GameObjects.EventCards import EventCards
from GameObjects.MainRAMVars import MainRAMVars
from GameObjects.GameDeck import GameDeck
#>python3 -m unittest Test.test_EC
class Test_test_EC(unittest.TestCase):
    def test_ECFunc112_A(self):
        Aev = EventCards(MainRAMVars(),[],GameDeck(),[])      
        Aev.playerFuncs = [4]
        Aev.PV.varsValue =np.array([1,2,0,1])
        Aev.ECFunc112()
        result = Aev.PV.varsValue[3]
        self.assertEqual(result,4)

    def test_ECFunc201_B(self):
        Bev = EventCards(MainRAMVars(),[],GameDeck(),[])
        Bev.PV.varsValue =np.array([10,10,10,1])
        Bev.reservedEC.append(201)
        Bev.ECFunc201()
        Bresult = len(Bev.reservedEC)
        self.assertGreater(Bresult,1)        

    def test_ECFunc201_C(self):
        Cev = EventCards(MainRAMVars(),[201],GameDeck(),[])
        Cev.PV.varsValue =np.array([-6,0,40,0])
        Cev.ECFunc201()
        Cresult = len(Cev.reservedEC)
        self.assertGreater(Cresult,1)        

if __name__ == '__main__':
    unittest.main()
