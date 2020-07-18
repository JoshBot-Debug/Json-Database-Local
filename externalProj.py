# from JsonDB.JsonDatabase import JsonDatabase, Create, New, Find
# import setuptools

# print(setuptools.find_packages())
# newDB = New("ReAnime")
# DB = JsonDatabase(newDB)


# DB = JsonDatabase(Find("ReAnime"))

# creator = Create()
# creator.table("Popular")
# creator.rows(["Name","Episode Name","Episode Number"])
# creator.values(["Re:Zero","Re:Zero Episode 1","1"])
# DB.create(creator)

# DB.select("Popular")
# DB.unique("Episode Name")
# DB.add("Name","Re:Zero")
# DB.add("Episode Name","Re:Zero Episode 3")
# DB.add("Episode Number","3")
# DB.flush()


# DB.select("Popular")
# # DB.one("Episode Name","Re:Zero Episode 2")
# DB.all("Name","Re:Zero")       # OR  DB.one("Name","Re:Zero")
# DB.where("Episode Number","3")
# # DB.update("Episode Name","Re:Zero Episode 2")
# value = DB.get("Episode Name")
# print(value)