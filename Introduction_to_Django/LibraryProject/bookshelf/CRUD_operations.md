book = Book("1984", "George Orwell", 1949)
book.save()

book1 = Book.objects.first()
print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949

book1 = Book.objects.get(title="1984")
book1.title = "Nineteen Eighty-Four"
book1.save()

book.delete()
# (1, {'bookshelf.Book': 1})