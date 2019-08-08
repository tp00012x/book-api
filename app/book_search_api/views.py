import json

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BookSearchApiView(APIView):
    def get(self, request):
        """
        API endpoint for GET requests.
        """
        query_params = request.query_params

        if query_params:
            try:
                response = self._open_library_response(**query_params)
            except requests.exceptions.RequestException:
                # Return response with error message and 503 status code
                # letting the user know that the service is unavailable.
                # Perhaps, the server is down for maintenance.
                return Response(
                    {
                        'Error Message': "Could not get a valid response from "
                                         "Open library's API"
                    },
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )

            # After getting the response successfully. We convert it into a
            # Python dictionary
            parsed_response = self._parse_response(response)

            # A response is sent containing a list of dictionary books that 'I
            # think' include the most relevant information for a book search.
            return Response({'books': self._books(parsed_response)},
                            status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'Error Message': 'No query params have been given for '
                                     'request'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def _books(parsed_response):
        """
        Generate a list of dictionary books containing a small sample for this
        exercise that will be displayed to the user.
        """
        books = []
        for book in parsed_response['docs']:
            book_data = {
                # After inspecting the response from open library, I will be
                # the "key"  to uniquely identify each book.
                'key': book.get('key').strip('/works/'),
                'title': book.get('title'),
                'open_library_url': "https://openlibrary.org{}".format(
                    book.get('key')),
                'author_name': book.get('author_name'),
                'edition_count': book.get('edition_count'),
            }
            books.append(book_data)

        return books

    @staticmethod
    def _open_library_response(
            **query_params: list) -> requests.models.Response:
        """
        Make request to open library api and return response.
        """
        open_library_url = 'http://openlibrary.org/search.json'
        response = requests.get(open_library_url, params=query_params)

        return response

    @staticmethod
    def _parse_response(response: requests.models.Response) -> dict:
        """
        Parse response to python dictionary.
        """
        return json.loads(response.text)
