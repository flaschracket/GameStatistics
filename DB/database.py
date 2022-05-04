import pyodbc
import copy

class database(object):
    """description of class"""
    def connectdb(self): 
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-D09H0RO;'
                              'Database=minibit;'
                              'Trusted_Connection=yes;')
        return conn


