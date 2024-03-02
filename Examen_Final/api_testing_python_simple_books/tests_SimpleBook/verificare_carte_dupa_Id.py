import unittest

import requests_SimpleBook.identificare_carte_dupa_Id_request



class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = requests_SimpleBook.identificare_carte_dupa_Id_request.BooksApi()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_by_id(self):
        response = self.books.get_api_books_filter()
        # self.assertEquals(response.status_code, 200, "Status code is not the same")
        random_book_id = response.json()[0]["id"]
        expected_book_name = response.json()[0]["name"]
        availability_book = response.json()[0]["available"]

        response = self.books.get_api_book_by_id(random_book_id)
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        self.assertEqual(response.json()["id"], random_book_id, "Book id is not the same")
        self.assertEqual(response.json()["name"], expected_book_name, "Book name is not the same")
        self.assertEqual(response.json()["available"], availability_book, "Book's availability is not the same")
