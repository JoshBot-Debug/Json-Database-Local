import os
import pickle
import pathlib


from JsonDB.interface.JsonDBInterface import JsonDBInterface
from JsonDB.interface.FindInterface import FindInterface

class Find(JsonDBInterface,FindInterface):


    __NAME = "[Model Find.py]"
    __DBDirectory = os.getcwd()+"\\JsonDatabase\\"


    def __init__(self,Name: str):
        print(f'{self.__NAME} Init')
        dbFileName = self.__DBDirectory+Name+".db"

        if not pathlib.Path(dbFileName).exists():
            raise FileNotFoundError(f"Your Database file was not found in '{dbFileName}'")

        # Open the .db file and unpickle it
        with open(dbFileName,"rb") as db:
            self.__Database = pickle.load(db)


    def _getDatabase(self):
        return self.__Database
   