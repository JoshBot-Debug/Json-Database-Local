from src.interface.JsonDBInterface import JsonDBInterface
from src.interface.CreateInterface import CreateInterface

class Create(JsonDBInterface,CreateInterface):

    __NAME = "[Model Create.py]"


    def __init__(self):
        self.__tableName = False
        self.__rowsList = False
        self.__valueList = False


    def table(self,Name: str):
        self.__tableName = Name


    def rows(self,Rows: list):
        self.__rowsList = Rows

    
    def values(self,Values: list):
        self.__valueList = Values


    def _getTable(self):
        return self.__tableName


    def _getRows(self):
        return self.__rowsList


    def _getValues(self):
        return self.__valueList