from typing import Optional
from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    desc: str
    rating: int

    def __init__(self, id, title, author, desc, rating):
        self.id = id
        self.title = title
        self.author = author
        self.desc = desc
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1, max_length=100)
    desc: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    class Config:
        json_schema_extra = {
            'example': {
                'id': 0,
                'title': 'New title',
                'author': 'book author',
                'desc': 'New book description',
                'rating': 4
            }
        }


BOOKS = [
    Book(1,'computer basics', 'ruby','nice book', 5),
    Book(2,'python', 'ruby','excellent book', 5),
    Book(3,'java', 'hp1','nice book', 3),
    Book(4,'csharp', 'hp2','nice book', 4),
    Book(5,'javascript', 'hp3','nice book', 2)
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):

    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(404, 'Item not found')


@app.get('/books/', status_code=status.HTTP_200_OK)
async def get_books_by_rating(rating: int = Query(gt=0, lt=6)):

    books_to_return = list()

    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)

    return books_to_return


@app.post('/books/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    print(type(book_request))  # create BookRequest object
    new_book = Book(**book_request.dict())  # dict() deprecated to model_dumps()
    print(type(new_book))  # creates Book class type
    BOOKS.append(new_book)


@app.put('/books/update_book/', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_req: BookRequest):

    for ix, book in enumerate(BOOKS):
        if book.id == book_req.id:
            BOOKS[ix] = book_req


@app.delete('/books/delete_book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):

    for ix, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(ix)
