from JsonDB.JsonDatabase import JsonDatabase, Create, New, Find
from JsonDB.jdbException.jdbException import ValueNotFoundError, KeyNotFoundError, ValueNotUniqueError


""" Create a new Database """
# DB = JsonDatabase(New("ReAnime"))


""" Find a Database """
# DB = JsonDatabase(Find("ReAnime"))


""" Create a new Table with keys """
DB = JsonDatabase(Find("ReAnime"))
creator = Create()
creator.table("Recent")
creator.keys(["Name","age"])
DB.create(creator)



""" Select a table in the Database and add some records"""
# DB = JsonDatabase(Find("ReAnime"))
# DB.select("Recent")


""" Here we set the key "Name" as the unique key """
# DB.unique("Name")


""" 
    Here we add multiple the records,
    Note that there is a custom exception class that can be used to catch particular exceptions. 
"""
# names = ["Tom","Dick","Harry"]
# for name in names:
#     try:
#         DB.add("Name",name)
#         DB.add("age","15")
#         DB.flush()
#     except ValueNotUniqueError as e:
#         print(e)


""" Here we add a single record to the table """
# DB = JsonDatabase(Find("ReAnime"))
# DB.select("Recent")
# DB.add("Name","DON")
# DB.add("age","20")
# DB.flush()


""" 
    Here we select an a table, then we get all the records that have the key "age" with a value of "20". 
    Then we search for the record that has the value "Joshua" and update the age to 21.
"""
# DB = JsonDatabase(Find("ReAnime"))
# DB.select("Recent")
# DB.all("age","20")
# DB.where("Name","Joshua",True)
# DB.update("age","21")

""" DB.get() is used to return a value so that you can check it. """
# print(DB.get("Name"))

