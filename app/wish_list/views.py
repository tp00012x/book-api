import json

import requests
from app.services import APIServices
from django.core import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import WishList
from .permissions import APIPermission
from .serializers import WishListSerializer


class WishListViewSet(viewsets.ModelViewSet):
    """
        A model ViewSet for viewing, creating and deleting Wish List objects.
    """
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [APIPermission]

    def create(self, request, *args, **kwargs):
        """
        We are manipulating the functionality of the create method because
        if the wish list object already exists. given the ol_id, we don't want
        to create a duplicate object, but just return the existing wish list.
        """
        ol_id = request.data.get('ol_id')

        try:
            wish_list_obj = WishList.objects.get(ol_id=ol_id)
        except WishList.DoesNotExist:
            # Catching the error that we raise if API request to the open
            # library API fails.
            try:
                create = super(WishListViewSet, self).create(
                    request, *args, **kwargs
                )
            except requests.exceptions.RequestException:
                return Response(
                    {
                        'Error Message': "Could not get a valid response from "
                                         "Open library's API"
                    },
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )

            return create

        return Response(serializers.serialize('python', [wish_list_obj, ]),
                        status.HTTP_200_OK)

    def perform_create(self, serializer):
        """
        After making the API call to open library, we can inject the desired
        data into the serializer.
        """
        ol_id = serializer.validated_data.get('ol_id')

        try:
            response = APIServices.get_book_details(ol_id)
        except requests.exceptions.RequestException:
            # In this case, we don't want to return a Response, because the
            # returned Response will be called by the ModelViewSet Create
            # method which will then create an object even if we didn't get
            # a valid response.
            raise requests.exceptions.RequestException()

        # Convert response object to Python dictionary
        parsed_response = json.loads(response.text)

        # We use the .get method to avoid getting an error if the key doesn't
        # exist in the parsed response. WishList was modeled in a way that any
        # of these values can be null except for ol_id.
        serializer.save(
            title=parsed_response.get('title'),
            publish_date=parsed_response.get('publish_date'),
            number_of_pages=parsed_response.get('number_of_pages'),
            physical_format=parsed_response.get('physical_format'),
            genres=parsed_response.get('genres'),
            isbn_13=parsed_response.get('isbn_13'),
            isbn_10=parsed_response.get('isbn_10'),
            description=parsed_response.get('description')
        )
