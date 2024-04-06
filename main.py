from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get('/books')
async def read_all_books():
    return BOOKS


# example of path parameter
@app.get('/books/author/{author}')
async def get_author_books(author: str):

    data = dict()
    book_list = list()

    for book in BOOKS:
        if book['author'].lower() == author.lower():
            book_list.append(book)

    data['author'] = author
    data['Books'] = book_list

    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)