__author__ = "Joshua Joseph Myers"
__copyright__ = "Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>"
__credits__ = ["Joshua Joseph Myers"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.1"
__maintainer__ = "Joshua Joseph Myers"
__email__ = "JoshuaMyersWebDev@gmail.com"
__status__ = "Production"

import os
import pathlib
import pickle
import json

from JsonDB.model.Create import Create
from JsonDB.model.New import New
from JsonDB.model.Find import Find
from JsonDB.interface.JsonDBInterface import JsonDBInterface
from JsonDB.interface.CreateInterface import CreateInterface
from JsonDB.interface.FindInterface import FindInterface
from JsonDB.interface.NewInterface import NewInterface

class JsonDB:


    __NAME = "[Controller JsonDB.py]"
    __DBDirectory = os.getcwd()+"\\JsonDB\\"


    def __init__(self,JsonDBInterface):
        print(f'{self.__NAME} Init')
        self.__interface = JsonDBInterface
        self.__selectedTableValues = None
        self.__selectedTable = None
        self.__selectedRow = None
        self.__selectedIndex = []

        self.__newRows = []
        self.__newValues = []
        self.__newUnique = []

        # If the Class passed in is New(), then run the create() method
        if isinstance(self.__interface,NewInterface):
            self.__interface._create()


        # Try getting the database, this will only work when you pass Find()
        if isinstance(self.__interface,FindInterface):
            self.__database = self.__interface._getDatabase()


    # This method is used to create a table
    def create(self,create: CreateInterface):

        # Check if the class passed here is an isinstance of the CreateInterface()
        if not isinstance(create, CreateInterface):
            raise Exception("You must pass an instance of the CreateInterface() to this method.")

        table = create._getTable()
        rows = create._getRows()
        values = create._getValues()

        if len(rows) != len(values):
            raise Exception(f"The number of rows is {len(rows)} and the number of values is {len(values)}. They need to be equal, check Create().rows() and Create().values()")

        if not table:
            raise Exception("You have not created a table.")
        
        if not rows:
            raise Exception("You have not created rows for your table.")
        
        if not values:
            raise Exception("You have not assigned values for your row.")

        self.__database._setTable(table)
        self.__database._setRows(rows,values)

        # Save the .db file
        self.__save()


    # This method is used to select a table in the Database()
    def select(self,Table: str):
        self.__selectedTableValues = self.__database._select(Table)

        if self.__selectedTableValues:
            self.__selectedTable = Table
        
        return self


    # This method will stop at the first index that finds a matching row and value
    def one(self,Row: str,Value: str):

        for index in self.__selectedTableValues:
            if self.__selectedTableValues[index][Row] == Value:
                self.__selectedIndex.append(index)
                return self

        raise Exception(f"Could not find any row that has the value '{Value}''")


    # This method will get every index that finds a matching row and value
    def all(self,Row: str,Value: str):

        for index in self.__selectedTableValues:
            if self.__selectedTableValues[index][Row] == Value:
                self.__selectedIndex.append(index)

        if not self.__selectedIndex:
            raise Exception(f"Could not find any row that has the value '{Value}'")
        
        return self


    # This method is used to update a table in the Database()
    def update(self,Row: str,Value: str):
        
        # Checks wheather we have an index
        if not self.__selectedIndex:
            raise Exception("You have to choose one or all, use JsonDB().one() or JsonDB().all()")
            exit(0)

        # Check if a table was selected
        if not self.__selectedTableValues:
            raise Exception("You have to select a table first, use JsonDB().select()")
            exit(0)
        
        for Index in self.__selectedIndex:
            keys = list(self.__selectedTableValues[Index])

            # Check if the row exists in the selected table
            if Row not in keys:
                raise Exception(f"The row {Row} does not exist in the selected table.\nExisting tables are {keys}")
                exit(0)

            # This passes all the verified data to the database
            self.__database._update(self.__selectedTable,Index,Row,Value)

            # Save the .db file
            self.__save()

        return self


    # This method is used to get a row from the selected table in the Database()
    def get(self,Row: str):
        
        # Checks wheather we have an index
        if not self.__selectedIndex:
            raise Exception("You have to choose one or all, use JsonDB().one() or JsonDB().all()")
            exit(0)

        # Check if a table was selected
        if not self.__selectedTableValues:
            raise Exception("You have to select a table first, use JsonDB().select()")
            exit(0)


        if Row not in self.__database._getTableAndRows()[self.__selectedTable]:
            raise Exception(f"The row {Row} does not exist in '{self.__selectedTable}', your choices are {self.__database._getTableAndRows()[self.__selectedTable]}")
            exit(0)


        if len(self.__selectedIndex) == 1:
            return self.__selectedTableValues[self.__selectedIndex[0]][Row]

        listOfResults = []
        for Index in self.__selectedIndex:
            listOfResults.append(self.__selectedTableValues[Index][Row])

        return listOfResults


    # This method is used to create a new row in a selected table
    def add(self, Row: str,Value: str):
        listOfRows = self.__database._getTableAndRows()[self.__selectedTable]

        if Row not in listOfRows:
            raise Exception(f"The row '{Row}' does not exist in the table {self.__selectedTable}")
            exit(0)
        
        self.__newRows.append(Row)
        self.__newValues.append(Value)

        return self


    # This method is used to save the new row
    def flush(self):
        listOfRows = self.__database._getTableAndRows()[self.__selectedTable]

        # Creates an empty Row with the new index and returns the index number
        Index = self.__database._newIndex(self.__selectedTable,self.__newUnique,self.__newValues)

        for i,Row in enumerate(self.__newRows):
            self.__database._update(self.__selectedTable,Index,Row,self.__newValues[i])

        # Save the .db file
        self.__save()

        return True


    # This method is used to set a value which should be unique
    def unique(self, Row: str):
        self.__newUnique.append(Row)
        return self


    # This method is used to find a record
    def where(self, Row: str, Value: str):
        for Index in self.__selectedIndex:
            if self.__selectedTableValues[Index][Row] == Value:
                self.__selectedIndex.clear()
                self.__selectedIndex.append(Index)
                return self

        raise Exception(f"Couldn't find '{Value}' in the selected key '{Row}'")


    # This method is used to update the Database(), usually called after changes are made to the Database()
    def __save(self):
        dbFileName = self.__DBDirectory+self.__database._getName()

        # Check if the JsonDB folder exists
        if not pathlib.Path(self.__DBDirectory).exists():
            raise Exception("The Database directory does not exist, please create a database first.")
            exit(0)

        # Check if a DB file exists
        if not pathlib.Path(dbFileName+".db").exists():
            raise Exception("The Database file does not exist, please create a database first.")
            exit(0)

        # Write the Database() to pickle
        with open(dbFileName+".db","wb") as db:
            pickleData = pickle.dump(self.__database,db, protocol=pickle.HIGHEST_PROTOCOL)

        # TMP
        with open(dbFileName+".json","w") as db:
            jsonData = json.dumps(self.__database.DATABASE,indent=4)
            db.write(jsonData)

        return True