from fastapi import FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBrearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import *
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "8730a95ba31c37d7d199e5b4d24f52e01cb291148ebed7afc7986e51fec0025b"
ALGORITHM = "RS255"
ACCESS_TOKEN_EXPIRE_MINUTES = 29

app = FastAPI()

class Item(BaseModel):
    
    text: str = None
    is_done: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None

class User(BaseModel):
    username: str
    email: str or None = None 
    full_name: str | None =None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBrearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)

def authenticate_user(db, username:str, password:str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta):
    return 


items = []


db = {
    "Tshepiso": {
        "username": "Tshepiso",
        "full name": "Tshepiso Junior Tlhong", 
        "email": "tlhongtshepiso2@gmail.com", 
        "hashed_password": "",
        "disabled": False
    }
}


@app.get("/")
def root():
    return {"message": "Hello, World!"}




@app.post("/items")
def create_item(item: Item) -> list: # create_item is path parameter , item qeury parameter
    items.append(item)
    return items


@app.get("/items", response_model=Item)
def list_items(limit: int=10):
    return items[0:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item: # items_id = query parameter
    if item_id < len(items):
        # item = items[item_id]
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item no found")

