import pyodbc
import copy
from DB.database import database
from GameObjects.GameSettings import *
from GameObjects.GameDeck import *

class dbGameSettings(object):
    """description of class"""

    def connectdb(self):
        db = database()
        conectionstring = db.connectdb()
        return conectionstring

    def insert_GameSettings(self,CurrentGameDeck):
        #CurrentGameDeck = GameDeck()
        myconn = self.connectdb()
        cursor = myconn.cursor()
        gs = GameSettings()
        cursor.execute("INSERT INTO minibit.dbo.GameSettings VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", 
                       ((gs.Testchangelog),gs.sampleQuantity,gs.winGoal,
                         gs.NrOfP,gs.maxRound,str(CurrentGameDeck.cardsCategory),
                         str(CurrentGameDeck.EC_Quantity),0,str(CurrentGameDeck.WCcardsCategory),
                         str(CurrentGameDeck.WC_Quantity),0,str(CurrentGameDeck.currentECdeck)))
        cursor.execute("SELECT @@IDENTITY")
        for row in cursor:
            settingsID = row[0]
        myconn.commit()
        return settingsID


