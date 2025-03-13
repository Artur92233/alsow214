import uuid


class Book:
    def __init__(self, author: str, title: str, ):
        self.author = author
        self.title = title
        self.inn: str = uuid.uuid4().hex


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, inn):
        for book in self.books:
            if inn == book.inn:
                self.books.remove(book)
                break

    def get_books(self):
        return self.books