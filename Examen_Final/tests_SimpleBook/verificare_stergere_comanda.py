import random
import unittest

from requests_SimpleBook.simple_books_requests import BooksApi


class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = BooksApi()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_delete_personal_order(self):
        response = self.books.get_api_books_filter()
        # self.assertEquals(response.status_code, 200, "Status code is not the same")
        random_book_id = response.json()[0]["id"]
        response = self.books.post_books_order(self.accessToken, random_book_id, "TMTA")

        order_id = response.json()["orderId"]
        response = self.books.delete_books_order(self.accessToken, order_id)
        self.assertEqual(response.status_code, 204, "Status code is not the same")

        response = self.books.get_books_orders_by_id(self.accessToken, order_id)
        self.assertEqual(response.status_code, 404, "Status code is not the same")
        self.assertEqual(response.json()["error"], f"No order with id {order_id}.", "Error message is not the same")