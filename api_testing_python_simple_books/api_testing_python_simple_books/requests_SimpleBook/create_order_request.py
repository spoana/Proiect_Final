import requests
import random


class CreateOrder:
    BASE_URL = "https://simple-books-api.glitch.me"
    ORDERS_ENDPOINT = "/orders"
    API_CLIENTS_ENDPOINT = "/api-clients/"

    def get_api_clients_route(self):
        return self.BASE_URL + self.API_CLIENTS_ENDPOINT

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

    def get_books_orders(self, access_token):
        url = self.get_orders_route()

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.get(url, headers=headers)

    def post_books_order(self, access_token, book_id, customer_name):
        url = self.get_orders_route()

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        return requests.post(url, json=body, headers=headers)
