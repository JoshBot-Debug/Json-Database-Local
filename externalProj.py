from JsonDB.JsonDatabase import JsonDatabase, Create, New, Find
from JsonDB.jdbException.jdbException import ValueNotFoundError, KeyNotFoundError, ValueNotUniqueError


# DB = JsonDatabase(New("ReAnime"))

DB = JsonDatabase(Find("ReAnime"))

# creator = Create()
# creator.table("Recent")
# creator.keys(["Name","age"])
# DB.create(creator)

DB.select("Recent")
DB.unique("Name")

<<<<<<< HEAD
# names = ["Hannah","Elsa","Joshua"]

# for name in names:
#     try:
#         DB.add("Name",name)
#         DB.add("age","20")
#         DB.flush()
#     except ValueNotUniqueError as e:
#         print(e)


DB.select("Recent")
DB.all("age","20")
try:
    DB.where("Name","Joshua",False)
except ValueNotFoundError as e:
    print(e)
# DB.all("Name","Joshua")
=======
names = ["Joshua","Hannah","Elsa"]

for name in names:
    DB.add("Name",name)
    DB.flush()


# DB.select("Recent")
# # DB.all("Name","Joshua")
>>>>>>> parent of 2d15f17... Renamed a few methods and documented them
# DB.delete()
print(DB.get("Name"))

# DB.select("Popular")

# DB.one("Episode Name","Domestic na Kanojo Episode 1")
# DB.all("Name","Re:Zero")       # OR  DB.one("Name","Re:Zero")
# DB.where("Episode Name","Re:Zero Episode 2")
# DB.delete()
# DB.update("Episode Number","2")
# value = DB.get("Episode Number")
# print(value)