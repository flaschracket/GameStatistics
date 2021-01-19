class Game():
    """description of class"""
    nofPlayers = 0
    CurrentRound = 0
    Winer = ''
    listofPlayers = []
    
    def WhoIsWinner(self):
        for x in range(len(self.listofPlayers)):
            if (self.listofPlayers[x].PlayerVars.Total > 49):
                self.Winer = self.listofPlayers[x].Name
            else:
                self.Winer = ''
        return(self.Winer)
