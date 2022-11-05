
from pydantic import BaseModel
from typing import Dict, List, Optional
from fastapi.routing import APIRouter

class Book(BaseModel):
    id: Optional[int]
    title: str
    authors: List[str]
    year: int

class UpdateBook(BaseModel):
    id: int
    authors: List[str]

class DeleteBookResponse(BaseModel):
    message: str


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

@router.post("/", response_model=Book, tags=["Books"], name="Create a book")
def create_book(book: Book):
    """
    Create a book and add it to the list of existing books.
    """
    book.id = len(books) + 1
    books.append(book)
    return book

@router.get("/", response_model=List[Book], tags=["Books"], name="Get all books from our database")
def get_books():
    """
    Get all books.
    """
    return books

@router.get("/{book_id}", response_model=Book, tags=["Books"], name="Get a book")
def get_book(book_id: int):
    """
    Get a book by its id.
    """
    return list(filter(lambda b: b.id == book_id, books))[0]

@router.put("", response_model=List[Book], tags=["Books"], name="Update a book")
def update_book(book: UpdateBook):
    """
    Update a book by its id.
    """
    old_book: Book = get_book(book.id)
    index: int = books.index(old_book)
    books[index].authors = book.authors
    return books

@router.delete("/{book_id}", response_model=DeleteBookResponse, tags=["Books"], name="Delete a book")
def delete_book(book_id: int):
    """
    Delete a book by its id.
    """
    books.pop(book_id - 1)
    return DeleteBookResponse(message = "Book deleted successfully")