class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")

# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

ClassTest.class_method()
ClassTest.static_method()

#Instance methods use the information in the class
#Static methods are used to place methods in a class, maybe makes more sense for structure. Used less than instance and class methods.

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("A Little Life", 1500)

print(book)
print(book2)
