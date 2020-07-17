from src.interface.JsonDBInterface import JsonDBInterface
from src.interface.CreateInterface import CreateInterface

class Create(JsonDBInterface,CreateInterface):

    __NAME = "[Model Create.py]"


    def __init__(self):
        self.tableName = False
        self.rowsList = False
        self.valueList = False


    def table(self,Name: str):
        self.tableName = Name


    def rows(self,Rows: list):
        self.rowsList = Rows

    
    def values(self,Rows: list):
        self.valueList = Rows


    def _getTable(self):
        return self.tableName


    def _getRows(self):
        return self.rowsList


    def _getValues(self):
        return self.valueList