from pymongo import MongoClient
import os

client = MongoClient(os.getenv('DB_URI'))
db = client['rick-morty-api']