from fastapi import FastAPI
from enum import Enum
import uvicorn

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
# Init
app = FastAPI(debug=True)
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning"}
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "lesnet"}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "othernet"}

@app.get("/files/{file_path:path}")
async def read_user_me(file_path: str):
    return {"file_path": file_path} 

# user/files/myfolder/file.txt

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")