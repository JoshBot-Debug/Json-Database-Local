class Database(object):


    def __init__(self,Name: str):
        self.__Name = Name
        self.__currentTable = ""
        self.__ExistingTables = []
        self.__TableAndRows = {}
        self.DATABASE = {
            self.__Name : {
                # For each table add a table here
            }
        }


    def _select(self, Table: str):

        # Check if the table exists in the Database()
        if Table not in self.__ExistingTables:
            raise Exception(f'The table "{Table}" does not exist in the Database\nExisting tables are {self.__ExistingTables}')
        
        # This checks if the table has a value, if it does it returns it.
        if self.DATABASE[self.__Name][Table]:
            return self.DATABASE[self.__Name][Table]

        # If the table does not have a value, then we are creating a new table so we just return true
        return True


    def _update(self, Table: str, Index: int, Row: str, Value: str):
        self.DATABASE[self.__Name][Table][Index][Row] = Value
        return True


    def _delete(self, Table: str, Index: list):
        selectedTable =  self.DATABASE[self.__Name][Table]
        
        # Delete the table from the Database() if index is none
        if not Index:
            self.DATABASE[self.__Name].pop(Table)
            self.__ExistingTables.remove(Table)
            return True

        # Delete the element from the Database() table
        for i in Index:
            selectedTable.pop(i)

        # Reset the keys
        self.DATABASE[self.__Name][Table] = {i: v for i, v in enumerate(selectedTable.values())}

        return True


    def _getName(self):
        return self.__Name


    def _getTableAndRows(self):
        return self.__TableAndRows


    def _setTable(self,Name: str):
        if Name not in self.__ExistingTables:
            self.__ExistingTables.append(Name)
            self.__currentTable = Name

            # Set the Refrence of Tables and Row names here
            self.__TableAndRows.update({self.__currentTable:[]})

            # Update the DB Dict
            self.DATABASE[self.__Name].update({Name: {}})

            return True
        raise Exception(f"The Table '{Name}' already exists")


    def _setRows(self,Rows: list):

        for i,row in enumerate(Rows):
            # Set the Row name Reference for the tables here
            self.__TableAndRows[self.__currentTable].append(row)


    def _newIndex(self,Table: str, Unique: list, Values: str):
        
        newIndex = len(self.DATABASE[self.__Name][Table])
        currentTable = self.DATABASE[self.__Name][Table]

        # Checks if the chosen unique value exists in the selected Table
        if Unique:
            for Row in currentTable:
                for UniRow in Unique:
                    # Check if the current table has values
                    if currentTable[Row]:
                        if currentTable[Row][UniRow] in Values:
                            raise Exception(f"The key '{UniRow}' already exists with the value '{currentTable[Row][UniRow]}'")
                            exit(0)


        # Create the index in the table
        currentTable.update({newIndex:{}})

        Rows = self.__TableAndRows[Table]

        for i,row in enumerate(Rows):
            # Update the DB Dict with empty values
            currentTable[newIndex].update({row: ""})

        # return the new index
        return newIndex