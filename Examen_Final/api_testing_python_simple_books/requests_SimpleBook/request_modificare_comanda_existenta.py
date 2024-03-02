import requests
import random



class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    ORDERS_ENDPOINT = "/orders"

    def _get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT

    def patch_books_order(self, access_token, order_id, new_value):
        URL = self._get_orders_route() + f"/{order_id}"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        body = {
            "customerName": new_value
        }

        return requests.patch(URL, json=body, headers=headers)
