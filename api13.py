from fastapi import FastAPI, Header
import uvicorn

# Init
app = FastAPI(debug=True)


@app.get("/items/")
async def read_items(*, ads_id: str = Header("abc")):
    return {"ads_id": ads_id}

@app.get("/itemsOne/")
async def read_items(*, user_agent: str = Header(None)):
    return {"user-agent": user_agent}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")