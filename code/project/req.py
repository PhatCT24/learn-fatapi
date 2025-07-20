from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Annotated

'''class Item(BaseModel):
    name: str
    description: str | None = None
    age: int 
    db: str | None = None

app = FastAPI()'''

'''@app.post("/items/")
async def create_item(item:Item):
    item_dict = item.dict()
    if item.name is not None:
        item_dict.update({"age": age})
    return item_dict'''

'''@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}'''

'''@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result'''

app = FastAPI()

''''@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''

'''@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''

'''@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

'''@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

'''@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items'''

'''@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items'''

'''@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

'''@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}