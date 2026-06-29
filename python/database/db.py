from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

print(os.getenv("URI"))
client = MongoClient(f"{os.getenv("URI")}")

database = client.get_database("resumeBuilder")

resumes = database["resumes"]
users = database["users"]
job_description = database["job_descriptions"]
ats_results = database["ats_results"]

try:
    client.admin.command("ping")
    print("Connected to MongoDB")

except Exception as e:
    print(f"Failed connection: {e}")