from rest_framework import serializers

from .models import WishList


class WishListSerializer(serializers.ModelSerializer):
    """
    Create serializer to parse model objects into a json response and
    vice versa. The only field that the request needs is the 'ol_id'
    field which we need to make the API request to the open library API.
    """
    class Meta:
        model = WishList
        fields = ('id', 'ol_id', 'title', 'publish_date', 'number_of_pages',
                  'physical_format', 'genres', 'isbn_13', 'isbn_10',
                  'description')
        read_only_fields = ('title', 'publish_date', 'number_of_pages',
                            'physical_format', 'genres', 'isbn_13', 'isbn_10',
                            'description')
