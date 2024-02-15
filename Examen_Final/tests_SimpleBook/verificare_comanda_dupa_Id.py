import unittest

from requests_SimpleBook.simple_books_requests import BooksApi


class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = BooksApi()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']
    def test_books_order_by_id(self):
        invalid_order_id = "InvalidOrderId"
        response = self.books.get_books_orders_by_id(self.accessToken, invalid_order_id)
        self.assertEqual(response.status_code, 404, "Status code is not the same")
        self.assertEqual(response.json()["error"], f"No order with id {invalid_order_id}.","Error message is not the same")

#acest test imi permite sa vad o comanda existenta. Necesita autentificare cu acces token