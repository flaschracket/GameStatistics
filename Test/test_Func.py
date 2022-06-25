import unittest
import copy
import numpy as np
from GameObjects.MainRAMVars import MainRAMVars
from GameObjects.Funcs import Funcs

class Test_test_Func(unittest.TestCase):
  #region buyfunc  
    def test_BuyFunc_A(self):
        var = MainRAMVars()
        var.varsValue = np.array([10,10,10,0])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],[201])
        ret = f.buyFunc()
        result= len(f.reservedEC)
        self.assertEqual(result, 0)

    def test_BuyFunc_B(self):
        var = MainRAMVars()
        var.varsValue = np.array([10,10,10,0])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],[201,201])
        ret = f.buyFunc()
        result= len(f.reservedEC)
        self.assertEqual(result, 1)

    def test_BuyFunc_C(self):
        var = MainRAMVars()
        var.varsValue = np.array([-6,2,5,1])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],[201])
        ret = f.buyFunc()
        result= len(f.reservedEC)
        self.assertEqual(result, 1)
#all vars have enough money. it should reduce from total
    def test_BuyFunc_D(self):
        var = MainRAMVars()
        var.varsValue = np.array([20,30,40,50])
        var.sumvars= var.calculatesumvars()
        f = Funcs(var,[],[201])
        ret = f.buyFunc()
        result= f.PV.varsValue[3]
        self.assertGreater(50, result)
#end region

#region reducePriceFromVars()
    def test_reducePriceFromVars_A(self):
        var = MainRAMVars()
        var.varsValue = np.array([10,2,2,50])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        self.assertEqual(var.sumvars,14)

    def test_reducePriceFromVars_B(self):
        var = MainRAMVars()
        var.varsValue = np.array([30,2,2,0])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        var.sumvars = var.calculatesumvars()
        self.assertEqual(var.sumvars,19)

    def test_reducePriceFromVars_C(self):
        var = MainRAMVars()
        var.varsValue = np.array([0,30,40,0])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        var.sumvars = var.calculatesumvars()
        self.assertEqual(var.sumvars, 55)

    def test_reducePriceFromVars_D(self):
        var = MainRAMVars()
        var.varsValue = np.array([0,0,40,0])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        var.sumvars = var.calculatesumvars()
        self.assertEqual(var.sumvars, 25)


    def test_reducePriceFromVars_E(self):
        var = MainRAMVars()
        var.varsValue = np.array([10,3,5,0])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        var.sumvars = var.calculatesumvars()
        self.assertEqual(var.sumvars,3)

    def test_reducePriceFromVars_F0(self):
        var = MainRAMVars()
        var.varsValue = np.array([5,2,50,0])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        var.sumvars = var.calculatesumvars()
        self.assertEqual(var.sumvars,42)

    def test_reducePriceFromVars_F1(self):
        var = MainRAMVars()
        var.varsValue = np.array([5,2,50,10])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        var.sumvars = var.calculatesumvars()
        self.assertEqual(var.varsValue[1],0)

    def test_reducePriceFromVars_F2(self):
        var = MainRAMVars()
        var.varsValue = np.array([5,2,50,10])
        var.sumvars = var.calculatesumvars()
        f= Funcs(var,[],[201])
        ret =f.reducePriceFromVars(15)
        var = copy.deepcopy(f.PV)
        var.sumvars = var.calculatesumvars()
        self.assertEqual(var.varsValue[1],0)

#buyfunc()

    
#end region
if __name__ == '__main__':
    unittest.main()
