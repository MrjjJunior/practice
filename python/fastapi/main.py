from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import *


app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

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