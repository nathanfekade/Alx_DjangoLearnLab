from .models import Author, Book, Library, Librarian

author = Author.objects.get(name = author_name)
books = Book.objects.filter(author=author)



library = Library.objects.get(name= library_name)


library = Library.objects.get(name=library_name)
librarian = library.librarian

