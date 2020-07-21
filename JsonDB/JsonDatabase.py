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

from JsonDB.jdbException.jdbException import ValueNotFoundError, KeyNotFoundError, ValueNotUniqueError

class JsonDatabase:
    """This class is used to manage the Database(). It accepts a NewInterface()
    to create a new Database() or a FindInterface() to find an existing Database().
    """

    __NAME = "[Controller JsonDatabase.py]"
    __DBDirectory = os.getcwd()+"\\JsonDatabase\\"


    def __init__(self,JsonDBInterface):
        print(f'{self.__NAME} Init')

        self.__selectedTableValues = None
        self.__selectedTable = None
        self.__selectedIndex = []

        self.__newKeys = []
        self.__newValues = []
        self.__newUnique = []

        # If the Class passed in is New(), then run the create() method
        if isinstance(JsonDBInterface,NewInterface):
            JsonDBInterface._create()


        # Try getting the database, this will only work when you pass Find()
        if isinstance(JsonDBInterface,FindInterface):
            self.__database = JsonDBInterface._getDatabase()


    # This method is used to create a new table in the Database()
    def create(self,create: CreateInterface):
        "This method is used to create a new table in the Database()"

        # Check if the class passed here is an isinstance of the CreateInterface()
        if not isinstance(create, CreateInterface):
            raise Exception("You must pass an instance of the CreateInterface() to this method.")

        table = create._getTable()
        rows = create._getRows()

        if not table:
            raise Exception("You have not created a table.")
        
        if not rows:
            raise Exception("You have not created rows for your table.")
        
        self.__database._setTable(table)
        self.__database._setRows(rows)

        # Save the .db file
        self.__save()


    # This method is used to select a single table in the Database()
    def select(self,Table: str):
        "This method is used to select a single table in the Database(), it returns all the records in the table."

        # Always have to clear the selectedIndex array before updatingit
        self.__selectedIndex.clear()

        self.__selectedTableValues = self.__database._select(Table)

        if self.__selectedTableValues:
            self.__selectedTable = Table

            if not isinstance(self.__selectedTableValues,bool) :
                self.__selectedIndex.clear()
                self.__selectedIndex = list(self.__selectedTableValues.keys())

        return self


    # This method will stop at the first index that finds a matching key and value
    def one(self,Key: str,Value: str):
        "This method will stop at the first index that finds a matching key and value"
        
        # Always have to clear the selectedIndex array before updatingit
        self.__selectedIndex.clear()

        for index in self.__selectedTableValues:
            if self.__selectedTableValues[index][Key] == Value:
                self.__selectedIndex.append(index)
                return self

        raise ValueNotFoundError(f"Could not find any key that has the value '{Value}''")



    # This method will get every index that finds a matching key and value
    def all(self,Key: str,Value: str):
        "This method will get every index that finds a matching key and value"

        # Always have to clear the selectedIndex array before updatingit
        self.__selectedIndex.clear()

        for index in self.__selectedTableValues:
            if self.__selectedTableValues[index][Key] == Value:
                self.__selectedIndex.append(index)

        if not self.__selectedIndex:
            raise ValueNotFoundError(f"Could not find any key that has the value '{Value}'")
        
        return self


    # This method is used to update a table in the Database()
    def update(self,Key: str,Value: str):
        "This method is used to update a value in the Database() after it has been found."

        # Checks wheather we have an index
        if not self.__selectedIndex:
            raise Exception("You have to choose one or all, use JsonDB().one() or JsonDB().all()")

        # Check if a table was selected
        if not self.__selectedTableValues:
            raise Exception("You have to select a table first, use JsonDB().select()")
        
        for Index in self.__selectedIndex:
            keys = list(self.__selectedTableValues[Index])

            # Check if the key exists in the selected table
            if Key not in keys:
                raise KeyNotFoundError(f"The key {Key} does not exist in the selected table.\nExisting tables are {keys}")

            # This passes all the verified data to the database
            self.__database._update(self.__selectedTable,Index,Key,Value)

            # Save the .db file
            self.__save()

        return self


    # This method is used to get a value from the selected table in the Database() using a key
    def get(self,Key: str):
        "This method is used to get a value from the selected table in the Database() using a key"
        
        # Checks wheather we have an index
        if not self.__selectedIndex:
            raise Exception("You have to choose one or all, use JsonDB().one() or JsonDB().all()")

        # Check if a table was selected
        if not self.__selectedTableValues:
            raise Exception("You have to select a table first, use JsonDB().select()")

        # Check if the key exists
        if Key not in self.__database._getTableAndRows()[self.__selectedTable]:
            raise KeyNotFoundError(f"The key {Key} does not exist in '{self.__selectedTable}', your choices are {self.__database._getTableAndRows()[self.__selectedTable]}")


        if len(self.__selectedIndex) == 1:
            return self.__selectedTableValues[self.__selectedIndex[0]][Key]

        listOfResults = []
        for Index in self.__selectedIndex:
            listOfResults.append(self.__selectedTableValues[Index][Key])

        return listOfResults


    # This method is used to create a new key in a selected table
    def add(self, Key: str,Value: str):
        "This method is used to create a new key in a selected table"

        listOfRows = self.__database._getTableAndRows()[self.__selectedTable]

        if Key not in listOfRows:
            raise KeyNotFoundError(f"The key '{Key}' does not exist in the table {self.__selectedTable}")
        
        self.__newKeys.append(Key)
        self.__newValues.append(Value)

        return self


    # This method is used to save a new record
    def flush(self):
        "This method is used to save a new record"

        listOfRows = self.__database._getTableAndRows()[self.__selectedTable]

        # Creates an empty Key with the new index and returns the index number
        Index = self.__database._newIndex(self.__selectedTable,self.__newUnique,self.__newValues)
        
        # If we received a dict, then we caught a ValueNotUniqueError
        if isinstance(Index,dict):
            # Clear the list of keys and values, this is done so that we can instantiate the Database once
            # and then in a for loop, keep using .add() and .flush()
            self.__newKeys.clear()
            self.__newValues.clear()
            raise ValueNotUniqueError(f"The key '{Index['error']['key']}' already exists with the value '{Index['error']['value']}'")


        for i,Key in enumerate(self.__newKeys):
            self.__database._update(self.__selectedTable,Index,Key,self.__newValues[i])

        # Save the .db file
        self.__save()

        # Clear the list of keys and values, this is done so that we can instantiate the Database once
        # and then in a for loop, keep using .add() and .flush()
        self.__newKeys.clear()
        self.__newValues.clear()

        return True


    # This method is used to set a key which should be unique in the table while updating it.
    def unique(self, Key: str):
        "This method is used to set a key which should be unique in the table while updating it."

        self.__newUnique.append(Key)
        return self


    # This method is used to find a record after selecting multiple records using the all() method.
    def where(self, Key: str, Value: str, Condition: bool):
        """This method is used to find records after selecting multiple records using the all() or select() method. Using a condition.
        Condition: is True by default, if set to False, it will find all the keys where the value is not
        what the given value is. NOTE: using .all() method before using .where() is faster than calling .where() after .select()
        """

        tmp = []
        # for index in the selected index(s) __selectedIndex
        for Index in self.__selectedIndex:
            # If we find a matching value return clear __selectedIndex
            # and append the index of the matching value.
            if not Condition:
                if self.__selectedTableValues[Index][Key] != Value:
                    tmp.append(Index)
            if Condition:
                if self.__selectedTableValues[Index][Key] == Value:
                    tmp.append(Index)

        if tmp:
            self.__selectedIndex.clear()
            self.__selectedIndex = tmp
            return self
        
        # If we find no matching value, raise an exception
        raise ValueNotFoundError(f"Couldn't find any records")


    # This method is used to delete a record or a table
    def delete(self):
        "This method is used to delete a record or a table."

        self.__database._delete(self.__selectedTable,self.__selectedIndex)

        # Save the .db file
        self.__save()


    # This method is used to update the Database(), usually called after changes are made to the Database()
    def __save(self):
        "This method is used to update the Database(), usually called after changes are made to the Database()."

        dbFileName = self.__DBDirectory+self.__database._getName()

        # Check if the JsonDB folder exists
        if not pathlib.Path(self.__DBDirectory).exists():
            raise Exception("The Database directory does not exist, please create a database first.")

        # Check if a DB file exists
        if not pathlib.Path(dbFileName+".db").exists():
            raise Exception("The Database file does not exist, please create a database first.")

        # Write the Database() to pickle
        with open(dbFileName+".db","wb") as db:
            pickleData = pickle.dump(self.__database,db, protocol=pickle.HIGHEST_PROTOCOL)

        # Writes a json file so that we can see the database
        with open(dbFileName+".json","w") as db:
            jsonData = json.dumps(self.__database.DATABASE,indent=4)
            db.write(jsonData)

        return True