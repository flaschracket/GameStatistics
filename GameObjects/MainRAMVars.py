
class MainRAMVars():
    """description of class"""
    """belongsto = player()"""
    VarA = 0
    VarB = 0
    VarC = 0
    Total = 0
    def _init_(self):
        VarA= 0
        VarB = 0
        VarC = 0
        Total = 0
        return self
    def print(self):
        print(' VarA = ' + str(self.VarA) + '')
        print(' VarB = ' + str(self.VarB) + '')
        print(' VarC = ' + str(self.VarB) + '')
        print(' Total = ' + str(self.Total) + '')
    
    def printinline(self):
        valuesare = ' VarA = ' + str(self.VarA) + ' VarB = ' + str(self.VarB) + ' VarC = ' + str(self.VarB) + ' Total = ' + str(self.Total)
        print(valuesare)