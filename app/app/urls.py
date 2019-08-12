from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wish_list.views import WishListViewSet

router = DefaultRouter()
router.register('wish-list', WishListViewSet, base_name='wish-list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/book-search/', include('book_search_api.urls'))
]
