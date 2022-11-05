# FastAPI Demonstrations for Backend@Home

## Make sure to install the dependencies in this subdirectory
Use `poetry install` in this directory `fastapi-demo` to install all the necessary packages.

## Use the demo's

Run the demos like this example:
`poetry run uvicorn fastapi_demo_1.main:app --reload`

### Example messages

```json
// Create
{
  "title": "Harry Potter and the Philosopher's Stone",
  "authors": [
    "J.K. Rowling"
  ],
  "year": 1997
}

// Update
{
  "id": 1,
  "authors": [
    "J.K. Rowling",
    "Nathan Segers"
  ]
}
```

### GraphQL

When running Demo 4, you can use GraphQL, this endpoint is available on `http://localhost:8000/graphql`

Try this query in the GraphiQL interface.
Explore the interface a bit more on your own, it contains some interesting concepts

```graphql
{
  books {
    title,
    id
  },
  book(id: 1) {
    title,
    id
  }
}
```

Also try this mutation

```graphql
mutation {
  addBook(
    title: "The Little Prince"
    author: "Antoine de Saint-Exupéry"
    year: 1943
  ) {
    title
  }
}
```