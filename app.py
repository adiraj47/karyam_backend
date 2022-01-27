from flask import Flask
from flask_restful import Api
from modules.applicant import Applicant

app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    api.add_resource(Applicant, "/applicant")
    app.run(host='0.0.0.0', port=80, debug=True)
