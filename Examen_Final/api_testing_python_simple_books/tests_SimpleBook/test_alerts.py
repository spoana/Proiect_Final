import unittest


class TestAlerts1(unittest.TestCase):
    class BooksApi:
        BASE_URL = "https://simple-books-api.glitch.me"
        API_CLIENTS_ENDPOINT = "/api-clients/"
        BOOKS_ENDPOINT = "/books"
        ORDERS_ENDPOINT = "/orders"
        STATUS_ENDPOINT = "/status"

     def get_status_route(self):
            return self.BASE_URL + self.STATUS_ENDPOINT

    def get_books_route(self):
            return self.BASE_URL + self.BOOKS_ENDPOINT

    def get_api_clients_route(self):
            return self.BASE_URL + self.API_CLIENTS_ENDPOINT

    def get_orders_route(self):
            return self.BASE_URL + self.ORDERS_ENDPOINT

   def setUp(self):
         print("")

     def tearDown(self):
         print("")

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
