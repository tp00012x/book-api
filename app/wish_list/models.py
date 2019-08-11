from django.db import models
from django.contrib.postgres.fields import ArrayField


class WishList(models.Model):
    """
    Creating model for WishList. Most of these fields can be null because
    the response received from the Open Library API may not include a lot of
    these fields.
    """
    ol_id = models.CharField(max_length=30)
    title = models.CharField(max_length=255, null=True, blank=True)
    publish_date = models.CharField(max_length=255, null=True, blank=True)
    number_of_pages = models.CharField(max_length=255, null=True, blank=True)
    physical_format = models.CharField(max_length=255, null=True, blank=True)
    # The ArrayField from the django postgres library was used to simplify tbe
    # project. Ideally, we would create new models that will have a foreign key
    # to the WishList model for different genres, ISBNs, etc.
    genres = ArrayField(
        models.CharField(max_length=255), null=True, blank=True
    )
    isbn_13 = ArrayField(
        models.CharField(max_length=13), null=True, blank=True
    )
    isbn_10 = ArrayField(
        models.CharField(max_length=10), null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
