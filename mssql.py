
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
    cursor.execute("INSERT INTO minibit.dbo.Game VALUES (?,?,?)", ((g.samplecounter),g.winer,Total))
    myconn.commit()
    return True

def updateGame(g):
    laststep = len(g.listofSteps)-1
    Total = str(g.listofSteps[laststep].P.playerVars.varsValue[3])
    myconn = connectdb()
    cursor = myconn.cursor()
    cursor.execute("UPDATE minibit.dbo.Game SET winner= ?, Total = ? where GameID =?", (g.winer,Total, (g.samplecounter)))
    myconn.commit()
    print("update game"+ str(Total))
    return True
def updateGameStoped(g):
    Total = str(g.listofSteps[g.currentStep-1].P.playerVars.varsValue[3])
    myconn = connectdb()
    cursor = myconn.cursor()
    cursor.execute("UPDATE minibit.dbo.Game SET winner= ?, Total = ? where GameID =?", (g.winer,Total, (g.samplecounter)))
    myconn.commit()
    print("update game"+ str(Total))
    return True


def insertStep(step,gameID):
    PV = copy.deepcopy(step.P.playerVars)
    #rowlist = (self.roundNr,self.stepNr,self.P.Name, PV.varsValue[0], PV.varsValue[1], PV.varsValue[2])
#    rowlist = rowlist + [PV.varsValue[3] , self.EC.currentEC,self.EC.nOfWC]
    #rowlist = rowlist+ [, nullList,self.playerDesicion ,playerPCStatus, self.P.roundCounter]
    #    rowlist = rowlist + [self.EC.ECName, playedWCName,self.winer,self.EC.playedEC, self.WC.playedWC]

    myconn = connectdb()
    cursor = myconn.cursor()
    

    cursor.execute("INSERT INTO minibit.dbo.Step VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(gameID),str(step.roundNr),str(step.stepNr),step.P.Name, str(PV.varsValue[0]), str(PV.varsValue[1]), str(PV.varsValue[2]),str(PV.varsValue[3]),step.EC.currentEC,step.EC.nOfWC,str(step.playerDesicion),step.EC.ECName))
    myconn.commit()
    return True