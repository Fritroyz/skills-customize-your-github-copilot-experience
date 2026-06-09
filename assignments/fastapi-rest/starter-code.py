from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI Item API")


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


# In-memory store
_items: List[Item] = []
_next_id = 1


def _get_item_index(item_id: int) -> Optional[int]:
    for i, item in enumerate(_items):
        if item.id == item_id:
            return i
    return None


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    idx = _get_item_index(item_id)
    if idx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return _items[idx]


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _next_id += 1
    _items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    idx = _get_item_index(item_id)
    if idx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    item.id = item_id
    _items[idx] = item
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    idx = _get_item_index(item_id)
    if idx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    _items.pop(idx)
    return None


# Example data for quick manual testing
if not _items:
    _items.extend([
        Item(id=1, name="Sample A", description="Example item A", price=9.99),
        Item(id=2, name="Sample B", description="Example item B", price=19.99),
    ])
    _next_id = 3
