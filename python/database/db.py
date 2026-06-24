from pymongo import MongoClient
import os

uri = f"mongodb+srv://Tshepiso:{os.environ.get("DB_PASSWORD")}@cluster0.72xvwbt.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

database = client.get_database("resumeBuilder")

print(database)