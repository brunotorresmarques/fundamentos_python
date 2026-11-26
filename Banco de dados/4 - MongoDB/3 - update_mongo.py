from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

old_value = {"level": "Intermediário"}
new_value = {"$set": {"level": "Iniciante"}}

mycol.update_one(old_value, new_value)

for x in mycol.find():
    print(x)