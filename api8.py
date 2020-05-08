from fastapi import FastAPI, Query, Path
import uvicorn

# Init
app = FastAPI(debug=True)


@app.get("/items/")
async def read_items(item_id: str = Query(..., min_length=2,max_length = 10, deprecated=True)):
    results = {"items": [{"item_id": "Pen"}, {"item_id": "Pencil"}] }
    if item_id:
        results.update({"item_id": item_id})
    return results

@app.get("/items/{item_id}")
async def read_items(item_id: str = Path(..., title = "item id", 
        desciption = "id for the item you want to retrieve", min_length=2,
        max_length = 10, regex="^Item\d{1,6}"),
        item: int = Query(..., gt=2, le = 10)):
    return {"item_id": item_id, "item":item}
    

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")