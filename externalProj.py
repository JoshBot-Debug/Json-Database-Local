from JsonDB.JsonDatabase import JsonDatabase, Create, New, Find
from JsonDB.jdbException.jdbException import ValueNotFoundError, KeyNotFoundError, ValueNotUniqueError


""" Create a new Database """
# DB = JsonDatabase(New("Json Database Website"))


""" Find a Database """
# DB = JsonDatabase(Find("Json Database Website"))


# """ Create a new Table with keys """
# DB = JsonDatabase(Find("Json Database Website"))
# creator = Create()
# creator.table("FAQ")
# creator.keys(["question","answere"])
# DB.create(creator)


""" Here we add a single record to the table """
# DB = JsonDatabase(Find("Json Database Website"))
# DB.select("FAQ")
# DB.add("question","How do I download JDB")
# DB.add("answere","Visit https://github.com/JoshBot-Debug/Json-Database-Local and download the .whl file that's inside the 'dist' folder.")
# DB.flush()


""" 
    Here we add multiple the records,
    Note that there is a custom exception class that
    can be used to catch exceptions. 
"""


DB = JsonDatabase(Find("Json Database Website"))

""" Select a table in the Database """
DB.select("FAQ")

""" Set the key "question" as unique to avoid any duplicate questions. """
DB.unique("question")

questions = ["How do I install JDB",
            "Are there any requirments to install JDB",
            "How do I delete a record"]

answeres = ["Copy the .whl file in your project directory,and run pip install jsonDB-0.0.1-py3-none-any.whl.",
            "JDB does not require any additional packages.",
            "Use the .delete() method to delete tables or records"]

for i,question in enumerate(questions):
    try:
        DB.add("question",question)
        DB.add("answere",answeres[i])
        DB.flush()
    except ValueNotUniqueError as e:
        # If there is a duplicate, skip it and print
        # out the key and value that was a duplicate
        print(e)


""" 
    Here we select an a table, then we get all the records that have the key "age" with a value of "20". 
    Then we search for the record that has the value "Joshua" and update the age to 21.
"""
DB = JsonDatabase(Find("Json Database Website"))
DB.select("FAQ")
DB.where("question","How do I delete a record",True)
DB.update("question","The correct question")
DB.update("answere","The correct answere")

""" DB.get() is used to return a value so that you can check it. """
# print(DB.get("answere"))

