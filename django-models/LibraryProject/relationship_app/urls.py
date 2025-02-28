from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('booklist/',list_books, name='booklist'),
    path('bookdetail/',LibraryDetailView.as_view(), name='book-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register', views.register, name='register')
]