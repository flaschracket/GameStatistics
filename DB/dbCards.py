import pyodbc
import copy
from DB.database import database

class dbCards(object):
    def connectdb(self):
        db = database()
        conectionstring = db.connectdb()
        return conectionstring

    def printallCards(self):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT * FROM minibit.dbo.Cards')
        for row in cursor:
            print(row)
        return True
    
    def selectWCQuantity(self,functionN):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT WCQuantity FROM [minibit].[dbo].[Cards] where FunctionNumber =' + str(functionN))
        for row in cursor.fetchone():
            q = row
            
        return q

    def selectAllCategoryID(self):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT ID FROM [minibit].[dbo].[Category]')
        cats = cursor.fetchall()
        return cats

    def selectAllCategoryQuantity(self):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT Quantity FROM [minibit].[dbo].[Category]')
        cats = cursor.fetchall()
        return cats

    def selectCardsofCategory(self, categoryID):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT FunctionNumber FROM [minibit].[dbo].[CardCategory] join [minibit].[dbo].[Cards] on [minibit].[dbo].[CardCategory].CardID = [minibit].[dbo].[Cards].ID where categoryID =' + str(categoryID))
        cards = cursor.fetchall()
        return cards


