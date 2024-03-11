import requests
import random



class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    ORDERS_ENDPOINT = "/orders"
    API_CLIENTS_ENDPOINT = "/api-clients/"
    BOOKS_ENDPOINT = "/books"



    def get_api_clients_route(self):
        return self.BASE_URL + self.API_CLIENTS_ENDPOINT


    def post_api_clients(self):
        URL = self.get_api_clients_route()

        #declare a random number to prevent error when creating a new user
        random_number = random.randint(1, 9999999999999999999)

        body = {
            "clientName": "Postman",
            "clientEmail": f"rexef{random_number}@tospage.com"
        }

        return requests.post(URL, json=body)

    def get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT

    def get_books_orders_by_id(self, access_token, order_id):
        URL = self.get_orders_route() + f"/{order_id}"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.get(URL, headers=headers)

    def get_books_route(self):
        return self.BASE_URL + self.BOOKS_ENDPOINT

    def get_api_books_filter(self, book_type="", limit=""):
        URL = self.get_books_route()

        query_params = {
            "type": book_type,
            "limit": limit}

        return requests.get(URL, params=query_params)

    def get_api_book_by_id(self, book_id):
        URL = self.get_books_route() + f"/{book_id}"
        return requests.get(URL)


