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
def get_item(item_id: int):
    if item_id < len(items):
        # item = items[item_id]
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item no found")