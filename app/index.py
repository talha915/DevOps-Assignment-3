from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

item_list = []

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    item_list.append(item.dict())
    return item.dict()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    res = [item if item.get('id') == item_id else 'Not found' for item in item_list]
    res = res[0] if len(res) == 1 else res
    return {"result": res}