book1 = Book.objects.get(title="1984")
print(book1.title, book1.author, book1.publication_year)
# 1984 George Orwell 1949