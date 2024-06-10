from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    full_name:str
    email:int
    disabled:bool


users_db = {
    "Coolser":{
        "username": "Coolser",
        "full_name": "Dilan Rojas",
        "email": "dilanrojasc6@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "Saris":{
        "username": "Saris",
        "full_name": "Sara Uribe",
        "email": "surubesa@gmail.com",
        "disabled": True,
        "password": "246810"
    }


}