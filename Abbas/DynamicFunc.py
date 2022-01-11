class DynamicFunc(object):
    """description of class"""
    def playaFunc(self,funcname,funcnumber):
        FuncName = funcname + str(funcnumber)
        getattr(self, FuncName)()
        return 


