from GameObjects.Player import Player

class WormCards():
    """description of class"""
    p = Player()
    totalWormCards = 10
    Name = ''

    def _init_(self):
        return('1') 
    def WCFunc0(self, p = Player()):
        p.PlayerVars.VarA = 0
        mystr = 'wf0:'
        return(mystr)
    def WCFunc1(self, p = Player()):
        p.PlayerVars.VarA = -1
        mystr = 'wf0:'
        return(mystr)
    def WCFunc2(self, p = Player()):
        p.PlayerVars.VarB = 0
        mystr = 'wf0:'
        return(mystr)
    def WCFunc3(self, p = Player()):
        p.PlayerVars.VarB = -1
        mystr = 'wf0:'
        return(mystr)
