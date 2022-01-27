from .firebase_connection import load_firebae
from flask_restful import Resource, reqparse
from flask_cors import  cross_origin

firebase = load_firebae()

class Applicant(Resource):
    @cross_origin()
    def post(self):
        user_data_parse = reqparse.RequestParser()
        user_data_parse.add_argument("email", type=str, required=True)
        user_data_parse.add_argument("platform", type=str, required=True)
        user_data_parse.add_argument("name", required=True, type=str)
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

        key = args["platform_mail"].replace("@", "").replace(".", "") + args["platform"]
        print(key)

        db = firebase.database()
        db.child("applicant").child(key).set(args)

        return {"Message": "response added"}


