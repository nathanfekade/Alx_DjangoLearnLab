from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic import DetailView, ListView


def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)
# class Library(ListView):