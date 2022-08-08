import unittest
from GameObjects.Player import *
from GameObjects.Bazar import *

class Test_test_Bazar(unittest.TestCase):

  
    def test_buyCPU_A(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([10,10,10,100])
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.buyCPU(player)
        result = len(player.playerReservedEC)
        self.assertEquals(result, 0)
        return

    def test_buyCPU_B(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([10,10,10,100])
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.buyCPU(player)
        result = player.playerVars.varsValue[3]
        self.assertEqual(result , 50)
        return

    def test_buyCPU_C(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([30,10,30,60])
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.buyCPU(player)
        result = player.playerVars.varsValue[3]
        self.assertEqual(result , 10)
        return
    
    def test_reducePriceFromVars_A(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([70,10,30,10])
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.reducePriceFromVars(player)
        result = player.playerVars.varsValue[0]
        self.assertEqual(result,20)
        return

    def test_reducePriceFromVars_B(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([50,10,30,10])
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.reducePriceFromVars(player)     
        result = player.playerVars.varsValue[0]
        self.assertEqual(result, 0)
        return

    def test_reducePriceFromVars_C(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([20,10,30,10])
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.reducePriceFromVars(player)
        result = player.playerVars.varsValue[0]
        self.assertEqual(result, 0)
        return

    def test_reducePriceFromVars_D(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([70,10,30,10])
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.reducePriceFromVars(player)        
        result = player.playerVars.varsValue[2]
        self.assertEqual(result, 30)
        return

    def test_reducePriceFromVars_E(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([70,10,30,10])
        player.playerVars.sumvars = player.playerVars.calculatesumvars()
        player.playerReservedEC.append([202])
        bazar = Bazar()
        bazar.reducePriceFromVars(player)
        player.playerVars.sumvars = player.playerVars.calculatesumvars()
        result = player.playerVars.sumvars
        self.assertEqual(result, 60)
        return


if __name__ == '__main__':
    unittest.main()
