import requests
import random



class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    ORDERS_ENDPOINT = "/orders"

    def get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT


    def post_books_order(self, access_token, book_id, customer_name):
        URL = self.get_orders_route()

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        return requests.post(URL, json=body, headers=headers)