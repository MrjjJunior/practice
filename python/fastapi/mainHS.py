from fastapi import FastAPI, HTTPException, Depends
import fastapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import *
from datetime import datetime, timedelta
from jose import JWTError, jwt #for plain text passwords
from passlib.context import CryptContext

# import jwt

SECRET_KEY = "$2b$12$g/WStY5UVjDRPCCj3KH1cOKHg4SSWz7tnfGT9cB5PAyLNQPjAGCpG"
ALGORITHM = "HS256" #RS256 or HS256
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
    full_name: str or None =None
    disabled: bool or None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


async def get_current_user(token: str = Depends(oauth_2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data = TokenData(username=username)

    except JWTError:
        raise credential_exception

    user = get_user(db, username=token_data.username)
    if user is None:
        raise credential_exception

    return user


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):

    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user



@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_402_UNAUTHORIZED,
                            detail="Incorrect username or password"
                            )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/users/me/items/")
async def read_own_me(current_user: User = Depends(get_current_user)):
    return [{"item_id": 1, "owner": current_user }]


items = []


db = {
    "Tshepiso": {
        "username": "Tshepiso",
        "full_name": "Tshepiso Junior Tlhong", 
        "email": "tlhongtshepiso2@gmail.com", 
        "hashed_password": "$2b$12$Qh5ebvgobaYaXffyWz0Uf.sGiXN4MXCes8/8JLsOe2rw3Fe.FhM1y",
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

pwd = get_password_hash("tstlh1")

print(pwd)