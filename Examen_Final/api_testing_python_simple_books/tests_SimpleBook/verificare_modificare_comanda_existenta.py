import random
import unittest

from requests_SimpleBook.verificare_comanda_existenta_requests import BooksApi

class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = BooksApi()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']


    def test_books_patch_order(self):
        response = self.books.get_api_books_filter()
        # self.assertEquals(response.status_code, 200, "Status code is not the same")
        random_book_id = response.json()[0]["id"]
        response = self.books.post_books_order(self.accessToken, random_book_id, "alvaa")

        order_id = response.json()["orderId"]
        random_number = random.randint(1, 9999999999999999999)
        new_owner_name = f"TMTA{random_number}"

        response = self.books.patch_books_order(self.accessToken, order_id, new_owner_name)
        self.assertEqual(response.status_code, 204, "Status code is not the same")


