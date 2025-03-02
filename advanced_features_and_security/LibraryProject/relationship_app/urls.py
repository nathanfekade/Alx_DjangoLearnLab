from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import admin_view, librarian_view, member_view, delete_book
from . import views
urlpatterns = [
    path('booklist/',list_books, name='booklist'),
    path('bookdetail/',LibraryDetailView.as_view(), name='book-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', admin_view, name='add_book'),  
    path('edit_book/', librarian_view, name='edit_book'),  
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),  
]