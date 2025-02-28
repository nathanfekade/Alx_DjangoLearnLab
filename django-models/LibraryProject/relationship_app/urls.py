from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('booklist/',list_books, name='booklist'),
    path('bookdetail/',LibraryDetailView.as_view(), name='book-detail')
]