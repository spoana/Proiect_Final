import unittest

from requests_SimpleBook.creare_comanda_request import BooksApi


class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = BooksApi()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_orders(self):
        response = self.books.get_books_orders(self.accessToken)
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        expected_number = 0
        self.assertEqual(len(response.json()), expected_number, "Number of orders is not the same")

