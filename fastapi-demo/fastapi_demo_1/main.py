from typing import Optional
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

from pydantic import BaseModel
from typing import List

# Without Pydantic
# class Book():
#     def __init__(self, title: str, authors: List[str], year: int, id = None):
#         self.id = id
#         self.title = title
#         self.authors = authors
#         self.year = year

# With Pydantic
class Book(BaseModel):
    id: Optional[int]
    title: str
    authors: List[str]
    year: int


books = []

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    book.id = len(books) + 1
    books.append(book)
    return book

@app.get("/books/", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    return list(filter(lambda b: b.id == book_id, books))[0]