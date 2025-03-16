class TestBook:

    def test_book_creation(self, book):
        assert book.inn
        assert book.author
        assert book.title

    def test_inn_in_book(self, book, another_book):
        assert book.inn != another_book.inn
