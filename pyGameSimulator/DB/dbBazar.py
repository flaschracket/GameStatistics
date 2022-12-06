import pyodbc
import copy
from DB.database import database

class dbBazar(object):
    """description of class"""
    def listofresult(self,resulttuple):
        i = 0
        resultlist = []
        ID = []
        Name = []
        Price = []
        SharedPrice = []
        for row in resulttuple:
            ID.append(row[0])
            Name.append(row[1])
            Price.append(row[2])
            SharedPrice.append(row[3])
        resultlist.append(ID)
        resultlist.append(Name)
        resultlist.append(Price)
        resultlist.append(SharedPrice)
    #    print("list of result")
    #    print(resultlist)
    #    print("******")
        return resultlist

    def connectdb(self):
        db = database()
        conectionstring = db.connectdb()
        return conectionstring
  
    def selectAll(self):
        myconn = self.connectdb()
        cursor = myconn.cursor()
        cursor.execute('SELECT * FROM [minibit].[dbo].[Bazar] where Type = 1')
        q = self.listofresult(cursor.fetchall())
       # print("select All result:")
       # print(cursor.fetchall())
        return q


