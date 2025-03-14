class TestLibrary:
    def test_name(self, library, book):
        assert library.name

    def test_remove_book(self, library, book):
        library.add_book(book)
        library.remove_book(book.inn)
        assert book not in library.books

    def test_get_books(self, library, book):
        library.add_book(book)
        assert book in library.books
