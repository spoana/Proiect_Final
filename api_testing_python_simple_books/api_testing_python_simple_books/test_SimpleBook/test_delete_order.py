import unittest

import sys
sys.path.append(r'C:\Users\Span\api_testing_python_simple_books')  # adăugați directorul proiectului în sys.path

import requests_SimpleBook.delete_order_request


class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = requests_SimpleBook.delete_order_request.DeleteOrder()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_delete_personal_order(self):
        response = self.books.get_api_books_filter()
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        random_book_id = response.json()[0]["id"]
        response = self.books.post_books_order(self.accessToken, random_book_id, "")

        order_id = response.json()["orderId"]
        response = self.books.delete_books_order(self.accessToken, order_id)
        self.assertEqual(response.status_code, 204, "Status code is not the same")
