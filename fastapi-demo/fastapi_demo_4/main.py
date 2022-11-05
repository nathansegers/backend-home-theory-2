from typing import List, Optional
from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Book:
    id: Optional[int]
    title: str
    authors: List[str]
    year: int

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

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[Book]:
        return books

    @strawberry.field
    def book(self, id: int) -> Book:
        return list(filter(lambda b: b.id == id, books))[0]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str, year: int, id: Optional[int] = None ) -> Book:
        if id is None:
            id = len(books) + 1
        book = Book(id=id, title=title, authors=[author], year=year)
        books.append(book)
        return book

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI(
    title="FastAPI Demo for Backend@Home",
    description="This is a demo of FastAPI",
    version="0.0.1",
)

app.include_router(graphql_app, prefix="/graphql")

