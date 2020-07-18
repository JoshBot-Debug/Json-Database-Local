from JsonDB.JsonDatabase import JsonDatabase, Create, New, Find
# import setuptools

# print(setuptools.find_packages())
# newDB = New("ReAnime")
# DB = JsonDatabase(newDB)


DB = JsonDatabase(Find("ReAnime"))

# creator = Create()
# creator.table("Recently added")
# creator.rows(["Name","Episode Name","Episode Number"])
# DB.create(creator)

# DB.select("Popular")
# DB.unique("Episode Name")
# DB.add("Name","Domestic na Kanojo")
# DB.add("Episode Name","Domestic na Kanojo Episode 2")
# DB.add("Episode Number","1")
# DB.flush()


DB.select("Recently added")

# DB.one("Episode Name","Domestic na Kanojo Episode 1")
# DB.all("Name","Re:Zero")       # OR  DB.one("Name","Re:Zero")
# DB.where("Episode Name","Re:Zero Episode 2")
DB.delete()
# # DB.update("Episode Number","2")
# # value = DB.get("Episode Number")
# # print(value)