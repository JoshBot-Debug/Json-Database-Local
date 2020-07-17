from JsonDB import JsonDB, Create, New, Find

# newDB = New("My First DB")
# DB = JsonDB(newDB)

# foundDb = Find("My First DB")
# DB = JsonDB(foundDb)

# creator = Create()
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

# DB.all("Name","Joshua")
# DB.one("Name","Joshua")
# DB.update("Age","21")
# DB.update("Age","A thousand years")
# print(DB.get("Age"))