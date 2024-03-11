import requests
import random


class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    API_CLIENTS_ENDPOINT = "/api-clients/"

    def get_api_clients_route(self):
        return self.BASE_URL + self.API_CLIENTS_ENDPOINT

    def post_api_clients(self):
        url = self.get_api_clients_route()

        # declare a random number to prevent error when creating a new user
        random_number = random.randint(1, 9999999999999999999)

        body = {
            "clientName": "Postman",
            "clientEmail": f"rexef{random_number}@tospage.com"
        }

        return requests.post(url, json=body)
