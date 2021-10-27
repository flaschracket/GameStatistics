import pyodbc
import copy
from DB.database import database

class dbCards(object):
    def listofresult(self,resulttuple):
        resultlist = [item[0] for item in resulttuple]
        return resultlist
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
        cats = self.listofresult(cursor.fetchall())
        return cats

    def selectAllCategoryQuantity(self):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT Quantity FROM [minibit].[dbo].[Category]')
        quantity = self.listofresult(cursor.fetchall())
        return quantity

    def selectCardsofCategory(self, categoryID):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT FunctionNumber FROM [minibit].[dbo].[CardCategory] join [minibit].[dbo].[Cards] on [minibit].[dbo].[CardCategory].CardID = [minibit].[dbo].[Cards].ID where categoryID =' + str(categoryID))
        cards = self.listofresult(cursor.fetchall())
        return cards


