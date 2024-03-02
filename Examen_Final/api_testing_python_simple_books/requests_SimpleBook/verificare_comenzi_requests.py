import requests


class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    ORDERS_ENDPOINT = "/orders"

    def get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT

    def get_books_orders(self, access_token):
        URL = self.get_orders_route()

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.get(URL, headers=headers)