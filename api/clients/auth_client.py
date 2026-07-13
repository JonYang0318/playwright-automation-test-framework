import requests
import os
from pathlib import Path
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(ROOT_DIR / ".env")


class AuthClient:


    BASE_URL = "https://reqres.in/api"


    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "x-api-key": os.getenv("REQRES_API_KEY"),

            "Content-Type": "application/json"

        })


    def login(self, payload):

        return self.session.post(

            f"{self.BASE_URL}/login",

            json=payload

        )
    
