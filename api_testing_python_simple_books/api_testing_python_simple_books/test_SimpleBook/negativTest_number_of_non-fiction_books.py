import unittest

import sys
sys.path.append(r'C:\Users\Span\api_testing_python_simple_books')  # adăugați directorul proiectului în sys.path

from requests_SimpleBook.query_parameters_request import QueryParams


class BooksTests(unittest.TestCase):

    def setUp(self) -> None:
        self.books = QueryParams()

    def test_books_filtered(self):
        response = self.books.get_api_books_filter(book_type="non-fiction", limit="2")
        expected_number = 4
        self.assertEqual(len(response.json()), expected_number, "")
