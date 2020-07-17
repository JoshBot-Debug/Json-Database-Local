
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
        
        return self.DATABASE[self.__Name][Table]


    def _update(self, Table: str, Index: int, Row: str, Value: str):
        self.DATABASE[self.__Name][Table][Index][Row] = Value
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
            self.DATABASE[self.__Name].update({Name: {0:{}}})

            return True
        raise Exception(f"The Table '{Name}' already exists")


    def _setRows(self,Rows: list,Values: list):
        currentTable = self.DATABASE[self.__Name][self.__currentTable]
        for i,row in enumerate(Rows):

            # Set the Row name Reference for the tables here
            self.__TableAndRows[self.__currentTable].append(row)

            # Update the DB Dict
            currentTable[0].update({row: Values[i]})


    def _newIndex(self,Table: str, Unique: str, Values: str):
        
        newIndex = len(self.DATABASE[self.__Name][Table])
        currentTable = self.DATABASE[self.__Name][Table]


        # Checks if the chosen unique value exists in the current Table
        if Unique:
            for Row in currentTable:
                if currentTable[Row][Unique] in Values:
                    raise Exception(f"A row already exists with the value '{currentTable[Row][Unique]}'")
                    exit(0)


        # Create the index in the table
        currentTable.update({newIndex:{}})

        Rows = self.__TableAndRows[Table]

        for i,row in enumerate(Rows):
            # Update the DB Dict with empty values
            currentTable[newIndex].update({row: ""})

        # return the new index
        return newIndex