from enum import Enum

from fastapi import FastAPI

app = FastAPI()

"""class Model(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: Model):
    if model_name.value == "alexnet":
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name is Model.lenet:
        return {"model_name": model_name, "message": "U mad bro?"}
    
    return {"model_name": model_name, "message": "I'm not mad"}"""

"""@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}"""

'''fake_items_db =[{"item_name": "Foo"}, {"item_name" :"Bar"},{"item_name" :"Baz"}]

@app.get("/items/")
async def read_item(skip:int = 0, limit: int = 10):
    return fake_items_db[ skip: skip + limit]'''


'''@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item'''

'''@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item'''

'''@app.get("/items/{item_id}")
async def read(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item'''

