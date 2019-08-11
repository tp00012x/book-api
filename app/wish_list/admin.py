from django.contrib import admin
from .models import WishList

# Register WishList to Admin, so the superuser can have the ability to
# manipulate the data as he/she pleases.
admin.site.register(WishList)
