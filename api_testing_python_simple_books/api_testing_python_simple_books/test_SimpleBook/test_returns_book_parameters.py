import unittest

import requests_SimpleBook.query_parameters_request


class BooksTests(unittest.TestCase):

    def setUp(self) -> None:
        self.books = requests_SimpleBook.query_parameters_request.QueryParams()

    def test_books_filtered(self):
        response = self.books.get_api_books_filter(book_type="", limit="")
        expected_number = 6
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")
