import requests
import random


class ListBooks:
    BASE_URL = "https://simple-books-api.glitch.me"
    BOOKS_ENDPOINT = "/books"
    API_CLIENTS_ENDPOINT = "/api-clients/"
    ORDERS_ENDPOINT = "/orders"

    def get_api_clients_route(self):
        return self.BASE_URL + self.API_CLIENTS_ENDPOINT

    def get_books_route(self):
        return self.BASE_URL + self.BOOKS_ENDPOINT

    def get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT

    def post_api_clients(self):
        url = self.get_api_clients_route()

        # declare a random number to prevent error when creating a new user
        random_number = random.randint(1, 9999999999999999999)

        body = {
            "clientName": "Postman",
            "clientEmail": f"rexef{random_number}@tospage.com"
        }

        return requests.post(url, json=body)

    def get_api_books_filter(self, book_type="", limit=""):
        url = self.get_books_route()

        query_params = {
            "type": book_type,
            "limit": limit}

        return requests.get(url, params=query_params)

    def get_books_orders(self, access_token):
        url = self.get_orders_route()

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.get(url, headers=headers)
