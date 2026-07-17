from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()



class LoginRequest(BaseModel):

    username: str

    password: str



@app.post("/login")
def login(data: LoginRequest):


    if (
        data.username == "test_user"
        and
        data.password == "password123"
    ):

        return {

            "token": "fake-jwt-token"

        }


    return {

        "message": "Invalid username or password"

    }