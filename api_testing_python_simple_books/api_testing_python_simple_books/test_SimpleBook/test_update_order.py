import random
import unittest

import sys
sys.path.append(r'C:\Users\Span\api_testing_python_simple_books')  # adăugați directorul proiectului în sys.path

import requests_SimpleBook.update_an_order_request


class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = requests_SimpleBook.update_an_order_request.UpdateOrder()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_patch_order(self):
        response = self.books.get_api_books_filter()
        # self.assertEquals(response.status_code, 200, "Status code is not the same")
        random_book_id = response.json()[0]["id"]
        response = self.books.post_books_order(self.accessToken, random_book_id, "valve")

        order_id = response.json()["orderId"]
        random_number = random.randint(1, 9999999999999999999)
        new_owner_name = f"TM TA{random_number}"

        response = self.books.patch_books_order(self.accessToken, order_id, new_owner_name)
        self.assertEqual(response.status_code, 204, "Status code is not the same")
