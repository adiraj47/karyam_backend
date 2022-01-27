import json
from flask import jsonify, Flask
from flask_restful import Resource, reqparse, Api
import os
from dotenv import load_dotenv
import pyrebase
import ast

load_dotenv()

app = Flask(__name__)
api = Api(app)

firebase_config = ast.literal_eval(os.environ["firebaseConfig"])

firebase = pyrebase.initialize_app(firebase_config)

db = firebase.database()


class Data_add(Resource):
    def post(self):
        user_data_parse = reqparse.RequestParser()
        user_data_parse.add_argument("name", required=True, type=str)
        user_data_parse.add_argument("email", required=True, type=str)
        user_data_parse.add_argument("phone", required=True, type=str)
        user_data_parse.add_argument("Gender", required=True, type=str)
        user_data_parse.add_argument("city", required=True, type=str)
        user_data_parse.add_argument("address", required=True, type=str)
        user_data_parse.add_argument("Primary_skill", required=True, type=str)
        user_data_parse.add_argument("Additional_skills", required=True, type=str)
        user_data_parse.add_argument("Experience", required=True, type=str)
        user_data_parse.add_argument("Current_Salary", required=True, type=str)
        user_data_parse.add_argument("Expected_salary", required=True, type=str)
        user_data_parse.add_argument("job_loc_1", required=True, type=str)
        user_data_parse.add_argument("job_loc_2", required=True, type=str)
        user_data_parse.add_argument("job_loc_3", required=True, type=str)
        user_data_parse.add_argument("job_post_pre_1", required=True, type=str)
        user_data_parse.add_argument("job_post_pre_2", required=True, type=str)
        user_data_parse.add_argument("job_post_pre_3", required=True, type=str)
        user_data_parse.add_argument("Linkdin_link", required=True, type=str)
        user_data_parse.add_argument("platform", type=str, required=True)
        user_data_parse.add_argument("platform_mail", type=str, required=True)

        args = user_data_parse.parse_args()

        name = args["name"]
        email_id = args["email"]
        phone = str(args["phone"])
        gender = args["Gender"]
        city = args["city"]
        address = args["address"]
        primary_skill = args["Primary_skill"]
        additional_skills = args["Additional_skills"]
        experience = str(args["Experience"])
        current_salary = str(args["Current_Salary"])
        expected_salary = str(args["Expected_salary"])
        job_loc_1 = args["job_loc_1"]
        job_loc_2 = args["job_loc_2"]
        job_loc_3 = args["job_loc_3"]
        job_post_pref_1 = args["job_post_pre_1"]
        job_post_pref_2 = args["job_post_pre_2"]
        job_post_pref_3 = args["job_post_pre_3"]
        linkdin_link = args["Linkdin_link"]
        platform_name = args["platform"]
        platform_mail = args["platform_mail"]

        print(args.values())
        print(args)

        db.child("details").push(*args)

        return jsonify(responses="Data Recorded")


api.add_resource(Data_add, '/')


if __name__ == "__main__":
    app.run()
