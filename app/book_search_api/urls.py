from django.urls import path

from .views import BookSearchApiView

app_name = 'book_search_api'

urlpatterns = [
    path('', BookSearchApiView.as_view(), name='get'),
]
