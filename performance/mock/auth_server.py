from fastapi import FastAPI
from pydantic import BaseModel
import time


app = FastAPI()



class LoginRequest(BaseModel):

    username: str

    password: str



# Login API
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



# Product API for stress testing
@app.get("/api/products")
def get_products():


    return {


        "products":[


            {
                "id":1,
                "name":"Laptop"
            },


            {
                "id":2,
                "name":"Phone"
            }


        ]

    }



# Search API for load testing
@app.get("/api/search")
def search():


    # 模擬 DB 查詢時間

    time.sleep(0.1)


    return {


        "status":"success",

        "result":[]


    }