import random
import requests


class DeleteOrder:
    BASE_URL = 'https://simple-books-api.glitch.me'
    API_CLIENTS_ENDPOINT = "/api-clients/"
    BOOKS_ENDPOINT = "/books"
    ORDERS_ENDPOINT = "/orders"
    STATUS_ENDPOINT = "/status"

    def get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT

    def get_api_clients_route(self):
        return self.BASE_URL + self.API_CLIENTS_ENDPOINT

    def get_books_route(self):
        return self.BASE_URL + self.BOOKS_ENDPOINT

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

    def post_books_order(self, access_token, book_id, customer_name):
        url = self.get_orders_route()

        headers = {
            'Authorization': f"Bearer {access_token}"
        }

        body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        return requests.post(url, json=body, headers=headers)

    def delete_books_order(self, access_token, order_id):
        url = self.get_orders_route() + f"/{order_id}"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.delete(url, headers=headers)
