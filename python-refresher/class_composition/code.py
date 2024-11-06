class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."
    

shelf = Bookshelf(300)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    

book = Book("The Secret History")
book2 = Book("A Little Life")
shelf = Bookshelf(book, book2)

print(shelf)
