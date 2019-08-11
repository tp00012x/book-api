import requests
from django.test import TestCase
from django.urls import reverse
from mock import patch
from rest_framework import status
from rest_framework.test import APIClient
from wish_list.models import WishList

BOOK_URL = reverse('wish-list-list')


class BookSearchApiViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_saving_book_to_wish_list(self):
        data = {
            "ol_id": "OL3966044M",
        }

        # I would patch this response to avoid flaky tests, but I will leave
        # here for now to test getting real data from open library's API
        res = self.client.post(BOOK_URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            WishList.objects.get(ol_id="OL3966044M").ol_id,
            data["ol_id"]
        )

    def test_saving_book_when_request_body_is_empty(self):
        data = {}

        res = self.client.post(BOOK_URL, data)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('requests.get')
    def test_get_book_details_when_response_from_open_library_fails(
            self, request_patch
    ):
        data = {
            "ol_id": "OL3966044M",
        }

        request_patch.side_effect = requests.RequestException

        res = self.client.post(BOOK_URL, data)

        self.assertEqual(res.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)

    def test_get_book(self):
        wish_list_obj = WishList.objects.create(ol_id="OL3966044M")

        res = self.client.get("/wish-list/{}/".format(wish_list_obj.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        wish_list_obj = WishList.objects.create(ol_id="OL3966044M")

        res = self.client.delete("/wish-list/{}/".format(wish_list_obj.id))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(WishList.DoesNotExist):
            WishList.objects.get(id=wish_list_obj.id)
