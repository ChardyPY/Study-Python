from book import Book

book1 = Book(300, False, 150)
book2 = Book(50, True, 75)
book3 = Book(250, True, 1000)

print(book1.price)
print(book3.for_sale)
print(book2.pages)
book2.openbook()