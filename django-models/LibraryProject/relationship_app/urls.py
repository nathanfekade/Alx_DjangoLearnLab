from django.urls import path
from . import views

urlpatterns = [
    path('booklist/',views.list_books, name='booklist'),
    path('bookdetail/',views.LibraryDetailView.as_view(), name='book-detail')
]