import unittest
import sys

sys.path.append(r'C:\Users\Span\api_testing_python_simple_books')  # adăugați directorul proiectului în sys.path

import requests_SimpleBook.negativscenario_params_request


class BooksTests(unittest.TestCase):

    def setUp(self) -> None:
        self.books = requests_SimpleBook.negativscenario_params_request.QueryParams1()

    def test_books_filtered(self):
        response = self.books.get_api_books_filter(book_type="fiction", limit="4")
        expected_number = 2

        self.assertEqual(len(response.json()), expected_number, "")
