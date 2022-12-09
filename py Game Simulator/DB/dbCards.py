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
        cursor.execute('SELECT WCQuantity FROM [minibit].[dbo].[Cards] where FunctionNumber =' + str(functionN) + 'and Type = 1')
        for row in cursor.fetchone():
            q = row       
        return q

    def selectAllCategoryID(self, type,myconn):
        cursor = myconn.cursor()
        cursor.execute('SELECT ID FROM [minibit].[dbo].[Category] where typenumber ='+ str(type))
        cats = self.listofresult(cursor.fetchall())
        return cats

    def selectAllCategoryQuantity(self,type):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT Quantity FROM [minibit].[dbo].[Category] where typenumber ='+ str(type))
        quantity = self.listofresult(cursor.fetchall())
        return quantity
    #typenumber: EC= 1 , 2 = WC

    def selectCardsofCategory(self, categoryID,typenumber):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT FunctionNumber FROM [minibit].[dbo].[CardCategory] join [minibit].[dbo].[Cards] on [minibit].[dbo].[CardCategory].CardID = [minibit].[dbo].[Cards].ID where categoryID =' + str(categoryID) +'and Type = '+ str(typenumber))
        cards = self.listofresult(cursor.fetchall())
        return cards


