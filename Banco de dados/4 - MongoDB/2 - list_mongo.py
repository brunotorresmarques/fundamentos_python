from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.dbposts

mycol = mydb.posts

# Retornar todos os documentos
result = mycol.find()

for r in result:
    pprint(r)