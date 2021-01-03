
import wikipedia
import pymongo
import os


MONGO_URI = 'mongodb://localhost'

#client = MongoClient(MONGO_URI)

#db = client['test']
#collection = db['post']

DATABASE="bot"
COLLECTION="post"


busqueda = input("inserte la busqueda que desea realizar : ")

results = wikipedia.search(busqueda)
        
myclient = pymongo.MongoClient(MONGO_URI)
db = myclient[DATABASE]
col = db[COLLECTION]
        
for i in results:
    try:
        wk = wikipedia.page(i)
        print()
        print(wk.title)
        print(wk.content)
        col.insert_one({"title":wk.title, "contenido": wk.content })
    except:
        print("post no encontrado")