import requests
import random


# pentru fiecare request se utilieaza acelasi URL;
# sunt create rute pentru pentru fiecare requests:


class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    API_CLIENTS_ENDPOINT = "/api-clients/"
    BOOKS_ENDPOINT = "/books"
    ORDERS_ENDPOINT = "/orders"
    STATUS_ENDPOINT = "/status"

    # rutele create pentru fiecare request
    def _get_status_route(self):
        return self.BASE_URL + self.STATUS_ENDPOINT

    def _get_books_route(self):
        return self.BASE_URL + self.BOOKS_ENDPOINT

    def _get_api_clients_route(self):
        return self.BASE_URL + self.API_CLIENTS_ENDPOINT

    def _get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT

    # 1.efectuare primul test - status code

    def get_api_status(self):
        URL = self._get_status_route()
        return requests.get(URL)

    # 2.retuneaza cartile dupa limita si tipul cartii (parametrii optionali)
    def get_api_books_filter(self, book_type="", limit=""):
        URL = self._get_books_route()

        query_params = {
            "type": book_type,
            "limit": limit
        }

        return requests.get(URL, params=query_params)

    # 3. returenaza o carte dupa id  - necesita token

    def get_api_book_by_id(self, book_id):
        URL = self._get_books_route() + f"/{book_id}"
        return requests.get(URL)

    # 4.Acces token valbil 7 zile
    def post_api_clients(self):
        URL = self._get_api_clients_route()

        # declare a random number to prevent error when creating a new user
        random_number = random.randint(1, 9999999999999999999)

        body = {
            "clientName": "Postman",
            "clientEmail": f"rexef{random_number}@tospage.com"
        }

        return requests.post(URL, json=body)

    # 5.Permite să vedem comenzile. Necesită autentificare.
    def get_books_orders(self, access_token):
        URL = self._get_orders_route()

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.get(URL, headers=headers)

    # 6.Permite sa identificam o carte dupa Id
    def get_books_orders_by_id(self, access_token, order_id):
        URL = self._get_orders_route() + f"/{order_id}"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.get(URL, headers=headers)

    # 7. Permite sa face o comanda de carti
    def post_books_order(self, access_token, book_id, customer_name):
        URL = self._get_orders_route()

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        return requests.post(URL, json=body, headers=headers)

    # 8. Permite modificare unei comenzi existente
    def patch_books_order(self, access_token, order_id, new_value):
        URL = self._get_orders_route() + f"/{order_id}"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        body = {
            "customerName": new_value
        }

        return requests.patch(URL, json=body, headers=headers)

# 9.Permite stergerea unei comenzi
    def delete_books_order(self, access_token, order_id):
        URL = self._get_orders_route() + f"/{order_id}"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.delete(URL, headers=headers)
