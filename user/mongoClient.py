from pymongo import MongoClient

client = MongoClient("0.0.0.0:27018", username="mongoadmin", password="secret")
db = client.test