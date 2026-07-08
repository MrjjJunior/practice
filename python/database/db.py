from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

print(os.getenv("URI"), "\n")
client = MongoClient(f"{os.getenv("URI")}")

database = client.get_database("ResumeBuilder")

resumes = database["resumes"]
users = database["users"]
job_description = database["job_descriptions"]
ats_results = database["ats_results"]

try:
    client.admin.command("ping")
    db = client.get_database("ResumeBuidler")
    print(db.get_collection("users"))
    print("Connected to MongoDB")

except Exception as e:
    print(f"Failed connection: {e}")