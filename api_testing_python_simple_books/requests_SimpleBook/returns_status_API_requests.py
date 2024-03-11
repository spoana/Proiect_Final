import requests


class BooksApi:
    BASE_URL = "https://simple-books-api.glitch.me"
    STATUS_ENDPOINT = "/status"

    def _get_status_route(self):
        return self.BASE_URL + self.STATUS_ENDPOINT

    def get_api_status(self):
        url = self._get_status_route()
        return requests.get(url)
