import os
from dotenv import load_dotenv
import pyrebase
import ast

load_dotenv()

firebase_config = ast.literal_eval(os.environ["firebaseconfig"])

firebase = pyrebase.initialize_app(firebase_config)

data = {

    "name": "aditya",
    "email": "fdajkfja@gmail.com",
    "phone": "8504589011",
    "Gender": "Male",
    "city": "Pune",
    "address": "akrudi",
    "Primary_skill": "python",
    "Additional_skills": "Ml",
    "Experience": "0",
    "Current_Salary": "0",
    "Expected_salary": "200000",
    "job_loc_1": "pune",
    "job_loc_2": "Mumbai",
    "job_loc_3": "Ahemdabad",
    "job_post_pre_1": "back-end",
    "job_post_pre_2": "front-end",
    "job_post_pre_3": "full-stack developer",
    "Linkdin_link": "adiraj47",
    "platform": "Google",
    "platform_mail": "rajpurohit.aditya43@gmail.com"
}

db = firebase.database()
string = data["platform_mail"] + data["platform"]
key = data["platform_mail"].replace("@", "").replace(".", "")
print(key)
print(data["platform_mail"])
# db.child("temp").child().push(data)
