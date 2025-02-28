from django.shortcuts import render
from .models import Author, Book, Librarian
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the context
        context = super().get_context_data(**kwargs)
        # Add the list of books for this library
        context['books'] = self.object.books.all()
        return context