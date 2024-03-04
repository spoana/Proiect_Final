import unittest

from requests_SimpleBook.request_retuneaza_lista_de_carti import BooksApi


class BooksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.books = BooksApi()


    def test_books_all_books(self):
        response = self.books.get_api_books_filter()
        self.assertEqual(response.status_code, 200, "Status code is not the same")

        expected_number = 6
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")
        self.assertEqual(response.json()[0]["id"], 1, "Id nu corespunde ")
        self.assertEqual(response.json()[0]["name"], "The Russian", "Acest nume nu exista")

#Acest test verifica numarul total de carti care este 6, status cod 200 ok ; daca adaug valoare mai mica testul pica;
#Nu este necesar sa folosesc acces token;
#valorile din assert pot fi modificate in functie de ce doresc sa verific legat de o carte: id, nume,etc.
#pot sa adaug cate asseruri am nevoie si sa verific dupa toti parametrii;