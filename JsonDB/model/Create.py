from JsonDB.interface.JsonDBInterface import JsonDBInterface
from JsonDB.interface.CreateInterface import CreateInterface

class Create(JsonDBInterface,CreateInterface):

    __NAME = "[Model Create.py]"


    def __init__(self):
        self.__tableName = False
        self.__rowsList = False


    def table(self,Name: str):
        self.__tableName = Name


    def rows(self,Rows: list):
        self.__rowsList = Rows

    def _getTable(self):
        return self.__tableName


    def _getRows(self):
        return self.__rowsList