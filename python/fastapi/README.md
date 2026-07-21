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
curl -X POST -H "Content-Type: application/josn" 'http://127.0.0.1:8000/items?item=apple'
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