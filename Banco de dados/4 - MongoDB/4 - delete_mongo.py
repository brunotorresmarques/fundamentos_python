from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

myquery = {"category": "Backend"}

x = mycol.delete_one(myquery)

print(f"{x.deleted_count} documento(s) excluído(s)")

