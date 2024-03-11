import unittest

from requests_SimpleBook.returns_status_API_requests import BooksApi


class BooksTests(unittest.TestCase):

    def setUp(self) -> None:
        self.books = BooksApi()

    def test_books_status(self):
        response = self.books.get_api_status()
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        self.assertEqual(response.json()['status'], "OK", "Response status is not the same")

#acest test trebuie sa returneze status API care va fi "ok" code:200 OK.
#acest test nu are nevoie de token acces.
#timp de raspuns -874 ms;
