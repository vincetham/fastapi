from fastapi import FastAPI, Query, Path, Body
import uvicorn
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None

# Init
app = FastAPI(debug=True)


@app.put("/items/{item_id}")
async def update_items(*, item_id: int = Path(..., title = "The ID of the item to get", ge=0, le=1000),
    item: Item = None, user: User, q: int = Body(...)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    results.update({"user": user})
    return results


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")