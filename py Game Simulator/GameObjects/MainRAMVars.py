import numpy as np
class MainRAMVars():
    """description of class"""
    """belongsto = player()"""
    
    
    def __init__(self):
        self.varsValue =np.array([0,0,0,0])
        self.Nullindex = []
        self.sumvars = 0
        return 
    
    def calculatesumvars(self):
        sumvars=0 
        ind = [0,1,2]
        sumvars = self.varsValue[0]+self.varsValue[1]+self.varsValue[2]
        return sumvars

#    def print(self):
 #       print(' Vars Value = ' + str(self.varsValue))
  #      return 
   # 
   # def printinline(self):
    #    valuesare = ' VarA = ' + str(self.varsValue[0]) + ' VarB = ' + str(self.varsValue[1]) + ' VarC = ' + str(self.varsValue[2]) + ' Total = ' + str(self.varsValue[3])
     #   print(valuesare)
      #  print('NUlls vars:')
       # print(self.Nullindex)