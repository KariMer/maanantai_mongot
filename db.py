
#python -m venv env

from multiprocessing import connection
from multiprocessing.connection import Client
from pymongo import MongoClient
# import pymongo
import passw
password = passw.PASSWORD
connection_string = "mongodb+srv://Kalle_Kani:<password>@clusterkm.5mt57.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
# client['AlbumDB'] Tämä koodi toimii myös alla
db = client.AlbumDB
albums = db.Albums

# Tulostetaan tietokannan collectioneiden nnimet:
print(db.list_collection_names())

# # kaikkien tietueiden haku
# result = albums.find()
# print(result)