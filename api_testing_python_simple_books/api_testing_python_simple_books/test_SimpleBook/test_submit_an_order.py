import unittest
import sys
sys.path.append(r'C:\Users\Span\api_testing_python_simple_books')  # adăugați directorul proiectului în sys.path

from requests_SimpleBook.submit_an_order_requests import SubmitOrder


class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = SubmitOrder()
        if self.accessToken != '':
            return
        self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_post_order(self):
        response = self.books.get_api_books_filter()
        # self.assertEquals(response.status_code, 200, "Status code is not the same")
        random_book_id = response.json()[0]["id"]
        response = self.books.post_books_order(self.accessToken, random_book_id, "PYTA4")
        self.assertEqual(response.status_code, 201, "Status code is not the same")
        self.assertEqual(response.json()["created"], True, "Created value is not the same")
