import unittest

import sys
sys.path.append(r'C:\Users\Span\api_testing_python_simple_books')  # adăugați directorul proiectului în sys.path

import requests_SimpleBook.check_book_by_Id_request



class BooksTests(unittest.TestCase):
    accessToken = ''

    def setUp(self) -> None:
        self.books = requests_SimpleBook.check_book_by_Id_request.BookId()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_by_id(self):
        response = self.books.get_api_books_filter()
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        random_book_id = response.json()[5]["id"]

        response = self.books.get_api_book_by_id(random_book_id)
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        self.assertEqual(response.json()["id"], random_book_id, "Book id is not the same")
