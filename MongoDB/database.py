from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sqlalchemy.orm.collections import collection

uri = "mongodb+srv://MobinR02:Te4MXxyaAr3LGJZm@cluster0.4tdbc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.LorestanUniv

student_collection = db["student"]
lecturer_collection = db["lecturer"]
course_collection = db["course"]
courseRegister_collection = db["CourseRegister"]
presentedCourses_collection = db["PresentedCourses"]
