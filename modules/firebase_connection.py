import os
from dotenv import load_dotenv
import pyrebase
import ast


def load_firebae():
    """

    :return:
    """
    load_dotenv()

    firebase_config = ast.literal_eval(os.environ["firebaseconfig"])

    firebase_connection = pyrebase.initialize_app(firebase_config)

    return firebase_connection


if __name__ == "__main__":
    firebase = load_firebae()
    firebase.auth()