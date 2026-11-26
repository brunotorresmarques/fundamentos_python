from pymongo import MongoClient

client = MongoClient()

mydb = client.dbposts
mycol = mydb.posts

post1 = {
    "title": "FastAPI",
    "category": "BackEnd",
    "author": {
        "name": "José",
        "email": "jose@email.com"
    }
}

post2 = {
    "title": "Pandas",
    "category": "Data Analisys",
    "level": "Intermediário",
    "author": {
        "name": "João",
        "email": "joao@email.com"
    }
}

result = mycol.insert_one(post2)
print("Documento incluído com sucesso!!")