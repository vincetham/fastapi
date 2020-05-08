from fastapi import FastAPI, Query
import uvicorn
from typing import List

# Init
app = FastAPI(debug=True)


@app.get("/items/")
async def get_items(item_id: List[str] = Query(..., title= "this api is to get items.", 
            description = "List of items to be returned.", min_length=2,max_length = 10, deprecated=True)):
    results = {"items": [{"item_id": "Pen"}, {"item_id": "Pencil"}] }
    if item_id:
        results.update({"item_id": item_id})
    return results

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")