from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_items_db = {
    1: {"id": 1, "name": "Item 1"},
    2: {"id": 2, "name": "Item 2"},
    3: {"id": 3, "name": "Item 3"},
}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item não existe")
    return fake_items_db[item_id]
