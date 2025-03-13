import pytest

from models import Book, Library


@pytest.fixture(scope='function')
def book() -> Book:
    return Book(author='J.K. Rowling', title='Harry Potter')


@pytest.fixture(scope='function')
def another_book() -> Book:
    return Book(author="George Orwell", title="1984")


@pytest.fixture(scope='function')
def library() -> Library:
    return Library(name='Одеська Бібліотека')
