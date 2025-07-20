'''ung dung web dobn gian cac thao tac crud'''
import random
from fastapi import FastAPI, HTTPException, status
from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator

app = FastAPI()

class Book(BaseModel):
    id: str
    name: str
    description: str | None = None
    price: float
    tax: float | None = None 
    tags: set[str] = set()

data = [
  {
    "id": "isbn-9780345391803",
    "name": "Dune",
    "description": "A science fiction novel about a young hero navigating a desert planet.",
    "price": 12.99,
    "tax": 1.30,
    "tags": ["science fiction", "novel", "space"]
  },
  {
    "id": "isbn-9780553293357",
    "name": "Foundation",
    "description": "The story of a galactic empire's decline and the rise of a new order.",
    "price": 9.99,
    "tax": 0.99,
    "tags": ["science fiction", "space opera", "classic"]
  },
  {
    "id": "imdb-tt0816692",
    "name": "Interstellar",
    "description": "A film about space exploration and human survival.",
    "price": 19.99,
    "tax": 0,
    "tags": ["science fiction", "movie", "space travel"]
  },
  {
    "id": "isbn-9780441172719",
    "name": "Neuromancer",
    "description": 0,
    "price": 10.50,
    "tax": 1.05,
    "tags": ["cyberpunk", "science fiction", "novel"]
  },
  {
    "id": "isbn-9780060850524",
    "name": "Brave New World",
    "description": "A dystopian novel exploring a futuristic society.",
    "price": 8.99,
    "tax": 0.90,
    "tags": ["dystopian", "science fiction", "classic"]
  },
  {
    "id": "imdb-tt0080684",
    "name": "Star Wars: The Empire Strikes Back",
    "description": "The second installment of the iconic Star Wars saga.",
    "price": 24.99,
    "tax": 2.50,
    "tags": ["science fiction", "movie", "space opera"]
  },
  {
    "id": "isbn-9780141439600",
    "name": "1984",
    "description": "A classic dystopian novel about totalitarianism.",
    "price": 7.99,
    "tax": 2,
    "tags": ["dystopian", "science fiction", "classic"]
  },
  {
    "id": "isbn-9780765317506",
    "name": "Ender's Game",
    "description": "A novel about a young boy training to fight an alien invasion.",
    "price": 11.49,
    "tax": 1.15,
    "tags": ["science fiction", "young adult", "space"]
  },
  {
    "id": "imdb-tt0133093",
    "name": "The Matrix",
    "description": "A cyberpunk film about a simulated reality.",
    "price": 17.99,
    "tax": 1.80,
    "tags": ["cyberpunk", "science fiction", "movie"]
  },
  {
    "id": "isbn-9780385333481",
    "name": "Snow Crash",
    "description": "gay",
    "price": 13.75,
    "tax": 1.38,
    "tags": ["cyberpunk", "science fiction", "novel"]
  },
  {
    "id": "isbn-9780061120084",
    "name": "Fahrenheit 451",
    "description": "A novel about a future where books are banned.",
    "price": 9.49,
    "tax": 3,
    "tags": ["dystopian", "science fiction", "classic"]
  },
  {
    "id": "imdb-tt0076759",
    "name": "Star Wars: A New Hope",
    "description": "The first film in the Star Wars franchise.",
    "price": 22.99,
    "tax": 2.30,
    "tags": ["science fiction", "movie", "space opera"]
  },
  {
    "id": "isbn-9780553382563",
    "name": "Hyperion",
    "description": "An epic science fiction novel blending mythology and space travel.",
    "price": 14.99,
    "tax": 1.50,
    "tags": ["science fiction", "space opera", "novel"]
  },
  {
    "id": "isbn-9780425083833",
    "name": "The Left Hand of Darkness",
    "description": "A novel exploring gender and society on an alien planet.",
    "price": 10.99,
    "tax": 1.10,
    "tags": ["science fiction", "novel", "social issues"]
  },
  {
    "id": "imdb-tt2543164",
    "name": "Arrival",
    "description": "A film about communication with extraterrestrial beings.",
    "price": 18.49,
    "tax": 0,
    "tags": ["science fiction", "movie", "linguistics"]
  }
]

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError("Invalid ID Format, please check again")
    return id 

@app.get("/books/")
async def read_books(id: Annotated[str | None, AfterValidator(check_valid_id)] = None,):
    if id :
        for items in data:
            if items["id"] == id:
                return items 
    else:
        return random.choice(data)
    
@app.put("/books/")
async def update_books(id: Annotated[str| None, AfterValidator(check_valid_id)] = None, book_update: Book = None):
    for item in data:
        if item["id"] == id:
            if book_update.name is not None:
                item["name"] = book_update.name
            if book_update.description is not None:
                item["description"] = book_update.description
            if book_update.price is not None:
                item["price"] = book_update.price
            if book_update.tax is not None:
                item["tax"] = book_update.tax
            if book_update.tags is not None:
                item["tags"] =book_update.tags
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.post("/books/")     
async def create_book(book: Book):
    for item in data:
        if item["id"] == book.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book with this ID already exists")
    data.append(book.model_dump())
    return book

@app.delete("/books/{id}")
async def delete_book(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    for item in data:
        if item["id"] == id:
            data.remove(item)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")