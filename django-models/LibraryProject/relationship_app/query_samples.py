from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name = author_name)
    books = Book.objects.filter(author=author)

    for book in books:
        print(f"{book.title}")

    return books

def books_in_library(library_name):

    library = Library.objects.get(name= library_name)
    books = library.books.all()

    for book in books:
        print(f"{book.title}")
    return books

def librarian_for_library(library_name):

    library = Library.objects.get(name=library_name)
    librarian = library.librarian

    print(f"{librarian.name}")

def run_queries():
    
    books_by_author('author')
    books_in_library('books')
    librarian_for_library('librarian')