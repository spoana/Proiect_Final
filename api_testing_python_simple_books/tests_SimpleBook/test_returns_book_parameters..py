import unittest

from requests_SimpleBook.query_parameters_request import BooksApi


class BooksTests(unittest.TestCase):


    def setUp(self) -> None:
        self.books = BooksApi()


    def test_books_filtered(self):
        response = self.books.get_api_books_filter(book_type="", limit="4")
        expected_number = 4
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")


#In acest test verificam cartile dupa tip si limita, statusul va fi ok ,deci exista 4 carti de tip fictiune;
#Acesti parametrii sunt optionali