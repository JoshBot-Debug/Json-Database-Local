import os
import pickle
import pathlib


from JsonDB.interface.JsonDBInterface import JsonDBInterface
from JsonDB.interface.FindInterface import FindInterface
from JsonDB.jdbException.jdbException import JdbFileNotFoundError

class Find(JsonDBInterface,FindInterface):
    "This class is used to find a Database() by name."

    __NAME = "[Model Find.py]"
    __DBDirectory = os.getcwd()+"\\JsonDatabase\\"


    def __init__(self,Name: str):
        print(f'{self.__NAME} Init')
        dbFileName = self.__DBDirectory+Name+".db"

        if not pathlib.Path(dbFileName).exists():
            raise JdbFileNotFoundError(f"Your Database file was not found in '{dbFileName}'")

        # Open the .db file and unpickle it
        with open(dbFileName,"rb") as db:
            self.__Database = pickle.load(db)


    def _getDatabase(self):
        return self.__Database
   