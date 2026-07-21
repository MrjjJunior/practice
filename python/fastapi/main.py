from fastapi import FastAPI, HTTPException
from typing import *
app = FastAPI()


items = []

@app.get("/")
def root():
    return {"message": "Hello, World!"}



@app.post("/items")
def create_item(item: str) -> list:
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item