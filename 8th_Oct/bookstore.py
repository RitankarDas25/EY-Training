from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Pydantic model for validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    in_stock: bool

#in memory database
books = [
    {"id": 1, "title": "Deep Learning", "author": "Ian Goodfellow", "price": 1200, "in_stock": True},
    {"id": 2, "title": "Python Tricks", "author": "Dan Bader", "price": 700, "in_stock": True},
    {"id": 3, "title": "Effective Java", "author": "Joshua Bloch", "price": 500, "in_stock": False},
    {"id": 4, "title": "Fluent Python", "author": "Luciano Ramalho", "price": 900, "in_stock": True},
]

# POST: Add a new book
@app.post("/books", status_code=201)
def add_book(new_book: Book):
    for book in books:
        if book["id"] == new_book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(new_book.dict())
    return {"message": "Book added successfully", "book": new_book}

# PUT: Update an existing book
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    if book_id != updated_book.id:
        raise HTTPException(status_code=400, detail="ID in path and body must match")
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books[i] = updated_book.dict()
            return {"message": "Book updated successfully", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE: Remove employee by ID
@app.delete("/books/{book_id}", status_code=200)
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully", "Book": book}
    raise HTTPException(status_code=404, detail="Book not found")

    raise HTTPException(status_code=404, detail="Book not found")

# GET: Search books (by author )
@app.get("/books/by_author/{author_name}",status_code=200)
def search_books_by_author(author_name :str ):
    filtered_books = books
    filtered_books=[book for book in filtered_books if author_name.lower() in book["author"].lower()]
    return {"books": filtered_books}

# GET: Search books (by price )
@app.get("/books/by_price/{max_price}",status_code=200)
def search_books_by_price(max_price :float):
    filtered_books = books
    filtered_books=[book for book in filtered_books if book["price"] <= max_price]
    return {"books": filtered_books}

# BONUS: Get available books
@app.get("/books/available")
def get_available_books():
    available = [book for book in books if book["in_stock"]]
    return {"available_books": available}

# BONUS: Get count of books
@app.get("/books/count")
def get_book_count():
    return {"count": len(books)}

# GET: Return all employees
@app.get("/books")
def get_all_books():
    return {"books": books}

# GET: Return single employee by ID
@app.get("/books/{id}")
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="book not found")



















