import unittest

from requests_SimpleBook.request_returns_list_of_books import ListBooks


class BooksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.books = ListBooks()

    def test_books_all_books(self):
        response = self.books.get_api_books_filter()
        self.assertEqual(response.status_code, 200, "Status code is not the same")

        expected_number = 6
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")
        self.assertEqual(response.json()[0]["id"], 1, "Id nu corespunde ")
        self.assertEqual(response.json()[0]["name"], "The Russian", "Acest nume nu exista")
