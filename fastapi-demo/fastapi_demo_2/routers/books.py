
from pydantic import BaseModel
from typing import List, Optional
from fastapi.routing import APIRouter

class Book(BaseModel):
    id: Optional[int]
    title: str
    authors: List[str]
    year: int

class UpdateBook(BaseModel):
    id: int
    authors: List[str]


books = [
    ## Define one book hardcoded to test quicker
    Book (
        id=1,
        title= "Harry Potter and the Philosopher's Stone",
        authors= [
            "J.K. Rowling"
        ],
        year= 1997
    ),
    Book (
        id=2,
        title= "Harry Potter and the Chamber of Secrets",
        authors= [
            "J.K. Rowling"
        ],
        year= 1998
    )
]

router = APIRouter()

@router.post("/", response_model=Book)
def create_book(book: Book):
    book.id = len(books) + 1
    books.append(book)
    return book

@router.get("/", response_model=List[Book])
def get_books():
    return books

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    return list(filter(lambda b: b.id == book_id, books))[0]

@router.put("", response_model=List[Book])
def update_book(book: UpdateBook):
    old_book: Book = get_book(book.id)
    index: int = books.index(old_book)
    books[index].authors = book.authors
    return books

@router.delete("/{book_id}")
def delete_book(book_id: int):
    books.pop(book_id - 1)
    return {"message": "Book deleted successfully"}