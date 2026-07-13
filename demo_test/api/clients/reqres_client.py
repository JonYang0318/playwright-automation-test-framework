import requests
import os
from pathlib import Path
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(ROOT_DIR / ".env")


class ReqresClient:

    BASE_URL = "https://reqres.in/api"


    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "x-api-key": os.getenv("REQRES_API_KEY"),
            "Content-Type": "application/json"
        })


    def get_user(self, user_id):

        return self.session.get(
            f"{self.BASE_URL}/users/{user_id}"
        )


    def create_user(self, payload):

        return self.session.post(
            f"{self.BASE_URL}/users",
            json=payload
        )


    def delete_user(self, user_id):

        return self.session.delete(
            f"{self.BASE_URL}/users/{user_id}"
        )