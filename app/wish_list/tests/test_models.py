from django.db import IntegrityError
from django.test import TestCase
from wish_list.models import WishList


class ModelTests(TestCase):

    def test_create_wish_list(self):
        """Test the creation of a book in the wish list"""
        wish_list = WishList.objects.create(
            ol_id='OL7261842M',
            title='The Fellowship of the Ring',
            publish_date="2001",
            number_of_pages=407,
            physical_format='Paperback',
            genres=['Action'],
            isbn_13=["9780007129706"],
            isbn_10=['000712970X'],
            description='The Fellowship of the Ring is the first...'
        )

        self.assertEqual(wish_list.title, 'The Fellowship of the Ring')

    def test_wish_list_missing_ol_field(self):
        with self.assertRaises(IntegrityError):
            WishList.objects.create(
                ol_id=None,
                title='The Fellowship of the Ring'
            )
