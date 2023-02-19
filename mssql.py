
import pyodbc
import copy

from GameObjects.SoftwarePatches import *

class mssql(object):
    """description of class"""


def connectdb(): 
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-D09H0RO;'
                          'Database=minibit;'
                          'Trusted_Connection=yes;')
    return conn

def listall():
    myconn = connectdb()
    cursor = myconn.cursor()
    cursor.execute('SELECT * FROM minibit.dbo.player')

    for row in cursor:
        print(row)
    return True
    


def update_GameSettings(firstdeck,ID):
    myconn = connectdb()
    cursor = myconn.cursor()
    strFirstdeck = " "+str(firstdeck) +" "
    cursor.execute("UPDATE minibit.dbo.GameSettings SET FirstDeck= ? where ID =?", 
                   strFirstdeck, ID)
    myconn.commit()
    return True

def insertGame(g):
    Total = '0'
    myconn = connectdb()
    cursor = myconn.cursor()
    cursor.execute("INSERT INTO minibit.dbo.Game VALUES (?,?,?,?,?,?)", 
                   (g.samplecounter,g.winer,Total,0,0,g.gamesettingsID))
    cursor.execute("SELECT @@IDENTITY")
    for row in cursor:
        GameID = row[0]
    myconn.commit()
    return GameID

def updateGame(g):
    Total = str(g.thisStep.P.playerVars.varsValue[3])
    myconn = connectdb()
    cursor = myconn.cursor()
    lastrounds= str(g.currentRound) 
    laststep = str(g.currentStep) 
    cursor.execute("UPDATE minibit.dbo.Game SET winner= ?, Total = ?, lastStep =?, lastRound =? where samplenumber =? and ID =?", 
                   (g.winer,Total,laststep,lastrounds, (g.samplecounter),g.gameID))
    myconn.commit()
    #print("Win Score = "+ str(Total))
    return True

def insertStep(step,gameID,samplenr):
    #prepare data

    varA = str(step.P.playerVars.varsValue[0])
    varB = str(step.P.playerVars.varsValue[1])
    varC = str(step.P.playerVars.varsValue[2])
    Total = str(step.P.playerVars.varsValue[3])
    nullList = str(step.P.playerVars.Nullindex)
    quantityRemainedCards = str(len(step.currentMixedCards))
    currentEC = str(step.EC.currentEC)
    #make list of  names from player functions
    funcObj = SoftwarePatches(step.P.playerVars, [],step.P.playerReservedEC)
    funcsname = ""
    listofFuncs = str(step.P.playerFuncs)
    strWCName= str(step.WC.playedWCName)
    strWCNr = str(step.WC.currentWC)
    strPlayerReservedEC = str(step.P.playerReservedEC)
    hardware = str(step.P.playerHardware)
    buyDesicions = str(step.buyDesicions)
    for item in step.P.playerFuncs:
        ind = funcObj.funcList.index(item)
        funcsname = funcsname+ " ** " + funcObj.funcName[ind] 
    

    #insert data
    myconn = connectdb()
    cursor = myconn.cursor()
    #step.printStep()
    insertstr = "INSERT INTO minibit.dbo.Step VALUES (?, ?, ?,?,?"
    insertstr = insertstr + ",?, ?, ?, ?, ?, "
    insertstr = insertstr + "?, ?, ?, ?, ?, "
    insertstr = insertstr + "?, ?, ?, ?, ?,"
    insertstr = insertstr + "?, ?,?)"

    cursor.execute(insertstr, (gameID,samplenr,str(step.roundNr),str(step.stepNr),step.P.Name,
                               varA,varB,varC,Total,currentEC,
                               step.EC.nOfWC,str(step.P.mydecision),
                               step.EC.ECName,nullList,str(step.P.PCStatus),
                               strWCName,quantityRemainedCards,strWCNr,
                               strPlayerReservedEC
                               , listofFuncs
                               , funcsname,buyDesicions,hardware
                               )) 
     #,'NULL'
    #test if the playing deck in EC and WC are needed
    # str(step.WC.playedWCName),str(len(step.EC.playingdeck)),str(step.WC.currentWC),
    myconn.commit()
    return True

