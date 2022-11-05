from typing import Optional
from fastapi import FastAPI
from .routers import books
app = FastAPI(
    title="FastAPI Demo for Backend@Home",
    description="This is a demo of FastAPI",
    version="0.0.1",
)

app.include_router(
    books.router,
    prefix="/books",
    tags=["Books"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}