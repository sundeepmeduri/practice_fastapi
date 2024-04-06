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


# get book by title. example of path parameter
@app.get('/books/{title}')
async def get_title_books(title: str):
    book_to_return = list()

    for book in BOOKS:
        if book.get('title').lower() == title.lower():
            book_to_return.append(book)

    return book_to_return


# example with query parameter
@app.get('/books/')
async def get_books_by_query_category(category: str):
    books_to_return = list()

    for book in BOOKS:
        if book['category'].lower() == category.lower():
            books_to_return.append(book)

    return books_to_return


# example of path parameter and query parameter
@app.get('/books/{author}/')
async def read_books_by_author_category(author: str,category: str):

    books_to_return = list()
    for book in BOOKS:
        if book['author'].lower() == author.lower() and book['category'].lower() == category.lower():
            books_to_return.append(book)

    return books_to_return


# example of path parameters
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
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)

