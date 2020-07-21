import os
import pickle
import pathlib

from JsonDB.interface.JsonDBInterface import JsonDBInterface
from JsonDB.interface.NewInterface import NewInterface
from JsonDB.Database import Database
from JsonDB.jdbException.jdbException import NewDatabaseError

class New(JsonDBInterface,NewInterface):
    "This class is used to create a new Database()"

    __NAME = "[Model New.py]"
    __DBDirectory = os.getcwd()+"\\JsonDatabase\\"

    def __init__(self,Name: str):
        print(f'{self.__NAME} Init')
        self.__db = Database(Name)
        self.__DbName = Name


    def _create(self):
        dbFileName = self.__DBDirectory+self.__DbName

        # Check if the JsonDatabase folder exists and create it if not
        if not pathlib.Path(self.__DBDirectory).exists():
            os.makedirs("JsonDatabase")

        # Check if a DB file already exists
        if pathlib.Path(dbFileName+".db").exists():
            raise NewDatabaseError("This database file already exists, please rename the file or delete the existing one.")

        # Write the Database() to pickle
        with open(dbFileName+".db","wb") as db:
            pickleData = pickle.dump(self.__db,db, protocol=pickle.HIGHEST_PROTOCOL)
        

        print(f'[New DB] : {self.__db}')
   