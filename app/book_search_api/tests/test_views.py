import json

import requests
from django.test import TestCase
from django.urls import reverse
from mock import patch
from rest_framework import status
from rest_framework.test import APIClient

BOOK_URL = reverse('book_search_api:get')


class BookSearchApiViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('requests.get')
    def test_get_book_search_when_query_params_are_given(self, request_patch):
        query_params = {
            "q": ["the lord of the rings"],
        }
        # To avoid any side effects or flaky tests such as having open
        # library's api not work properly, the API GET request has been mocked.
        request_patch.return_value.text = json.dumps({
            "docs": [
                {
                    "key": "OL8527426W",
                    "title": "Lord of the Rings",
                    "author_name": [
                        "Cedco Publishing"
                    ],
                    "edition_count": 5,
                    "publishers": [
                        "Cedco Publishing Company"
                    ],
                    "characters": None,
                    "place": None,
                    "languages": [
                        "eng"
                    ]
                }
            ]
        })

        res = self.client.get(BOOK_URL, query_params)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual("Lord of the Rings", res.data['books'][0]['title'])

    def test_get_book_search_when_query_params_are_not_given(self):
        query_params = {}
        res = self.client.get(BOOK_URL, query_params)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('requests.get')
    def test_get_book_search_when_response_from_open_library_fails(
            self, request_patch
    ):
        query_params = {
            "q": ["the lord of the rings"],
        }
        request_patch.side_effect = requests.RequestException

        res = self.client.get(BOOK_URL, query_params)

        self.assertEqual(res.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
