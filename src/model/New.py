import os
import pickle
import pathlib

from src.interface.JsonDBInterface import JsonDBInterface
from src.interface.NewInterface import NewInterface
from src.Database import Database

class New(JsonDBInterface,NewInterface):

    __NAME = "[Model New.py]"
    __DBDirectory = os.getcwd()+"\\JsonDB\\"

    def __init__(self,Name: str):
        print(f'{self.__NAME} Init')
        self.__db = Database(Name)
        self.__DbName = Name


    def _create(self):
        dbFileName = self.__DBDirectory+self.__DbName

        # Check if the JsonDB folder exists and create it if not
        if not pathlib.Path(self.__DBDirectory).exists():
            os.makedirs("JsonDB")

        # Check if a DB file already exists
        if pathlib.Path(dbFileName+".db").exists():
            raise Exception("This database file already exists, please rename the file or delete the existing one.")
            exit(0)

        # Write the Database() to pickle
        with open(dbFileName+".db","wb") as db:
            pickleData = pickle.dump(self.__db,db, protocol=pickle.HIGHEST_PROTOCOL)
        

        print(f'[New DB] : {self.__db}')
   