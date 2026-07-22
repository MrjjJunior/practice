Routes define defferent URL. 
## Install fastapi
```
pip install fastapi
```
 

## running app with uvicorn

```
uvicorn main:app --reload
```

## update using curl

POST
```
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
```

GET
```
curl -X GET http://127.0.0.1:8000/items/0
```

## Rasing Errors
Learn about HTTP codes 

```
from fastapi import HTTPExceptions

def func():
    
    raise HTTPException(status_code=<code>, details=<string>)

```

## Requests and Path Parameters

limit is a parameter in list_items
```
curl -X GET 'http://127.0.0.1:8000/items?limit=3'
```

Still learning BaseModel
### Base Model
update values while there is a base model

```
curl -X POST -H "Content-Type: application/json" -d '{"text": "apple"}' 'http://127.0.0.1:8000/items'
```


Base model is the blueprint of a schema.
```
class Item(BaseModel):
    text: str = None
    is_done: bool = False
```

Removing the default values you make the key a value a requirement, you have to put in a value or it fails

```
class Item(BaseModel):
    text: str
    is_done: bool = False
```

## Response Models

response model will return the json in the predetermined way/ blue print.
```
@app.get("/items/{item_id}", response_model=Item)
```
