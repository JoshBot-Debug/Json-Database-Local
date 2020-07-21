from JsonDB.JsonDatabase import JsonDatabase, Create, New, Find
from JsonDB.jdbException.jdbException import ValueNotFoundError, KeyNotFoundError, ValueNotUniqueError


# DB = JsonDatabase(New("ReAnime"))

DB = JsonDatabase(Find("ReAnime"))

# creator = Create()
# creator.table("Recent")
# creator.keys(["Name","age"])
# DB.create(creator)

# DB.select("Recent")
# DB.unique("Name")

# names = ["Tom","Dick","Harry"]

# for name in names:
#     try:
#         DB.add("Name",name)
#         DB.add("age","15")
#         DB.flush()
#     except ValueNotUniqueError as e:
#         print(e)


# DB.select("Recent")
# DB.add("Name","DON")
# DB.add("age","20")
# DB.flush()


DB.select("Recent")
DB.all("age","20")
DB.where("age","20",True)
DB.where("Name","Joshua",True)
DB.update("age","21")

print(DB.get("Name"))

