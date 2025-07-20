from typing import Annotated
from pydantic import AfterValidator
from fastapi import FastAPI, Path, Query

app = FastAPI()

'''@app.get("/items/{items_id}")
async def read_item(item_id = Annotated[int, Path(title="item_to_get_id")], q:Annotated[str|None,Query(alias="item-query")] = None,):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results'''

'''@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=5)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results'''

'''@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results'''

