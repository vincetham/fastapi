from fastapi import FastAPI
import uvicorn

# Init
app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/home")
async def myhome():
    return {"message": "home page"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")