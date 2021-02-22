
class MainRAMVars():
    """description of class"""
    """belongsto = player()"""
    VarsValue = [0,0,0,0]
    NullVars = ['-','-','-','-']
    
    def print(self):
        print(' Vars Value = ' + str(*self.VarsValue))
        return 
    def printinline(self):
        valuesare = ' VarA = ' + str(self.VarsValue[0]) + ' VarB = ' + str(self.VarsValue[1]) + ' VarC = ' + str(self.VarsValue[2]) + ' Total = ' + str(self.VarsValue[3])
        print(valuesare)