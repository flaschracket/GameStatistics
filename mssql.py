
import pyodbc
import copy
import GameObjects.Game
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

def insertGame(g):
    Total = '0'
    myconn = connectdb()
    cursor = myconn.cursor()
    cursor.execute("INSERT INTO minibit.dbo.Game VALUES (?,?,?,?,?)", ((g.samplecounter),g.winer,Total,0,0))
    myconn.commit()
    return True

def updateGame(g):
    Total = str(g.thisStep.P.playerVars.varsValue[3])
    myconn = connectdb()
    cursor = myconn.cursor()
    lastrounds= str(g.currentRound) 
    laststep = str(g.currentStep) 
    cursor.execute("UPDATE minibit.dbo.Game SET winner= ?, Total = ?, lastStep =?, lastRound =? where samplenumber =?", 
                   (g.winer,Total,laststep,lastrounds, (g.samplecounter)))
    myconn.commit()
    print("updating game, total is: "+ str(Total))
    return True

def insertStep(step,gameID):
    PV = copy.deepcopy(step.P.playerVars)
    myconn = connectdb()
    cursor = myconn.cursor()
    insertstr = "INSERT INTO minibit.dbo.Step VALUES (?, ?, ?, ?, ?, "
    insertstr = insertstr + "?, ?, ?, ?, ?, "
    insertstr = insertstr + "?, ?, ?, ?, ?, "
    insertstr = insertstr+ "?, ?)"
    step.EC.ECPlayedcollection.elements()
    plyECstr = str(step.EC.ECPlayedcollection)
    plyECstr = "' "+plyECstr + " '"
    cursor.execute(insertstr, (str(gameID),str(step.roundNr),str(step.stepNr),step.P.Name, str(PV.varsValue[0]),str(PV.varsValue[1]),str(PV.varsValue[2]),str(PV.varsValue[3]),
                              step.EC.currentEC,step.EC.nOfWC,str(step.playerDesicion),step.EC.ECName,str(PV.Nullindex),
                              str(step.P.PCStatus),str(step.WC.playedWCName),
                               ','.join(str(e) for e in step.EC.ECPlayedcollection),''.join(str(e) for e in step.WC.playedWC)))
    myconn.commit()
    return True