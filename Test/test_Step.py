import unittest
from GameObjects.Player import *
from GameObjects.Step import *
from GameObjects.GameDeck import *
from GameObjects.GameSettings import *
class Test_test_Step(unittest.TestCase):
    gs = GameSettings()
    def test_BuyHardware_A(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([30,10,30,60])
        player.playerReservedEC.append([202])
        gd = GameDeck()
        step = Step(p = player,currentgamedeck =gd)
        step.buyHardware()
        result = step.P.playerVars.varsValue[3]
        self.assertEqual(result, 10)
        return

    def test_BuyHardware_B(self):
        player = Player('tester')
        player.playerVars.varsValue = np.array([30,10,30,60])
        player.playerReservedEC.append([202])
        gd = GameDeck()
        step = Step(p = player,currentgamedeck =gd)
        step.buyHardware()
        result = len(step.P.playerReservedEC)
        self.assertEqual(result, 0)
        return

if __name__ == '__main__':
    unittest.main()
