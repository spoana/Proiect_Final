import unittest

from requests_SimpleBook.request_parametrii_carte import BooksApi


class BooksTests(unittest.TestCase):


    def setUp(self) -> None:
        self.books = BooksApi()


    def test_books_filtered(self):
        response = self.books.get_api_books_filter(book_type="non-fiction", limit="2")
        expected_number = 5
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")
