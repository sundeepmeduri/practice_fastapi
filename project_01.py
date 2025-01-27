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


@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put('/books/update_book')
async def update_book(update_book=Body()):

    for i, book in enumerate(BOOKS):
        if book['title'].lower() == update_book['title'].lower():
            BOOKS[i] = update_book

@app.delete('/books/delete_book')
async def delete_book(delete_book=Body()):

    for i, book in enumerate(BOOKS):
        if book['title'].lower() == delete_book['title'].lower():
            BOOKS.pop(i)


