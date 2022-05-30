import unittest
import numpy as np
from GameObjects.MainRAMVars import MainRAMVars
from GameObjects.Funcs import Funcs

class Test_test_Func(unittest.TestCase):
    
    def test_BuyFunc_A(self):
        var = MainRAMVars()
        var.varsValue = np.array([10,10,10,0])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],0,0,[201])
        ret = f.buyFunc()
        result= len(f.reservedEC)
        self.assertEqual(result, 0)

    def test_BuyFunc_B(self):
        var = MainRAMVars()
        var.varsValue = np.array([10,10,10,0])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],0,0,[201,201])
        ret = f.buyFunc()
        result= len(f.reservedEC)
        self.assertEqual(result, 1)

    def test_BuyFunc_C(self):
        var = MainRAMVars()
        var.varsValue = np.array([-6,2,5,1])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],0,0,[201])
        ret = f.buyFunc()
        result= len(f.reservedEC)
        self.assertEqual(result, 1)
#all vars have enough money. it should reduce from total
    def test_BuyFunc_D(self):
        var = MainRAMVars()
        var.varsValue = np.array([20,30,40,50])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],0,0,[201])
        ret = f.buyFunc()
        result= f.PV.varsValue[3]
        self.assertGreater(50, result)

if __name__ == '__main__':
    unittest.main()
