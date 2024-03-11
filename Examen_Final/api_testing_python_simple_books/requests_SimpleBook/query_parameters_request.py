import requests


class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    API_CLIENTS_ENDPOINT = "/api-clients/"
    BOOKS_ENDPOINT = "/books"

    def get_books_route(self):
        return self.BASE_URL + self.BOOKS_ENDPOINT

    def get_api_books_filter(self, book_type="", limit=""):
        url = self.get_books_route()

        query_params = {
            "type": book_type,
            "limit": limit}

        return requests.get(url, params=query_params)
