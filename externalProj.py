from JsonDB import JsonDB, Create, New, Find

newDB = New("ReAnime")
DB = JsonDB(newDB)


# DB = JsonDB(Find("ReAnime"))

# creator = Create()
# creator.values()
# creator.table("First Table")
# creator.rows(["Name","Age","DOB"])
# creator.values(["Joshua","21","21 Feb 1998"])
# DB.create(creator)

# creator = Create()
# creator.table("Second Table")
# creator.rows(["Skills","Height","Weight"])
# creator.values(["Programmer","5.8","60 kgs"])
# DB.create(creator)

# DB.select("First Table")
# DB.unique("Name")
# DB.new("Name","Elsa")
# DB.new("Age","24")
# DB.new("DOB","29 Mar")
# DB.flush()

# DB.select("First Table")
# DB.all("Name","Joshua")       # OR  DB.one("Name","Joshua")
# DB.update("Age","21")
# age = DB.get("Age")