from .models import Author, Book, Library, Librarian

try:
    author = Author.objects.get(name="John Doe")
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author}:")
    for book in books_by_author:
        print(f"- {book}")
except Author.DoesNotExist:
    print("Author 'John Doe' not found")

try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()  
    print(f"Books in {library}:")
    for book in books_in_library:
        print(f"- {book}")
except Library.DoesNotExist:
    print("Library 'Central Library' not found")

try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library}:")
    print(f"- {librarian}")
except Library.DoesNotExist:
    print("Library 'Central Library' not found")
except Librarian.DoesNotExist:
    print("No librarian assigned to 'Central Library'")