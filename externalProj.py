from JsonDB.JsonDatabase import JsonDatabase, Create, New, Find


# DB = JsonDatabase(New("ReAnime"))

DB = JsonDatabase(Find("ReAnime"))

# creator = Create()
# creator.table("Recent")
# creator.keys(["Name"])
# DB.create(creator)

DB.select("Recent")
DB.unique("Name")

names = ["Joshua","Hannah","Elsa"]

for name in names:
    DB.add("Name",name)
    DB.flush()


# DB.select("Recent")
# # DB.all("Name","Joshua")
# DB.delete()

# DB.select("Popular")

# DB.one("Episode Name","Domestic na Kanojo Episode 1")
# DB.all("Name","Re:Zero")       # OR  DB.one("Name","Re:Zero")
# DB.where("Episode Name","Re:Zero Episode 2")
# DB.delete()
# DB.update("Episode Number","2")
# value = DB.get("Episode Number")
# print(value)