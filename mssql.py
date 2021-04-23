
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
    #GameID = cursor.lastrowid
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
    print("updating game, total is: "+ str(Total))
    return True

def insertStep(step,gameID,samplenr):
    #print(str(step.WC.WCPlayedcollection))
    PV = copy.deepcopy(step.P.playerVars)
    myconn = connectdb()
    cursor = myconn.cursor()
    insertstr = "INSERT INTO minibit.dbo.Step VALUES (?, ?, ?,?,?, "
    insertstr = insertstr + "?, ?, ?, ?, ?, "
    insertstr = insertstr + "?, ?, ?, ?, ?, "
    insertstr = insertstr+ "?, ?, ?)"

    cursor.execute(insertstr, (gameID,samplenr,str(step.roundNr),str(step.stepNr),step.P.Name, str(PV.varsValue[0]),
                              str(PV.varsValue[1]),str(PV.varsValue[2]),str(PV.varsValue[3]),str(step.EC.currentEC),
                              step.EC.nOfWC,str(step.playerDesicion),step.EC.ECName,str(PV.Nullindex), str(step.P.PCStatus),str(step.WC.playedWCName),
                               str(len(step.EC.playingdeck)),'NULL'))
    
    myconn.commit()
    return True

   #         str(np.arange(0,500,0.5).tolist() , ','.join(str(e) for e in list(step.EC.playingdeck))   ,' , '.join(str(el) for el in step.WC.WCPlayedcollection))