from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = {
    1: {"id": 1, "name": "Item 1"},
    2: {"id": 2, "name": "Item 2"}
}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in fake_db:
        return fake_db[item_id]
    raise HTTPException(status_code=404, detail="Item não existe")
