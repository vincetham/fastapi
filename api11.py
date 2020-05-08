from fastapi import FastAPI, Query, Path, Body
import uvicorn
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str = Field(None, title="description of field", max_length=150)
    price: float = Field(..., gt=0, le=100, description="field checking")
    tax: float = None
    tags: Set[int] = []
    image: Image = None

class Offer(BaseModel):
    name: str
    description: str = Field(None, title="description of field", max_length=150)
    price: float = Field(..., gt=0, le=100, description="field checking")
    items: List[Item]

class User(BaseModel):
    username: str
    full_name: str = None

# Init
app = FastAPI(debug=True)


@app.put("/items/{item_id}")
async def update_items(*, item_id: int, offer: Offer):
    results = {"item_id": item_id, "offer": Offer}
    return results


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")