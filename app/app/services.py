import requests


class APIServices(object):
    @staticmethod
    def get_book_details(ol_id: str) -> requests.models.Response:
        """
        Make request to open library to get the details of a specific book.
        """
        open_library_url = "http://openlibrary.org/work/{}.json".format(ol_id)
        response = requests.get(open_library_url)

        return response

    @staticmethod
    def get_books(**query_params: list) -> requests.models.Response:
        """
        Make request to open library api and return response containing book
        results.
        """
        open_library_url = 'http://openlibrary.org/search.json'
        response = requests.get(open_library_url, params=query_params)

        return response
