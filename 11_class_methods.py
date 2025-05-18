# iss program main humnay book class banai or class variable banaya jo sb objects kayliye common hota hai
# or class method banaya jo new book create honay pr class variable ko 1 say increase krayga.

class Book:

    total_books = 0

    def __init__(self, title):
        self.title = title           # constructor call hua title initalize hua
        Book.increment_book_count()  # class method call hua after initialization 


    @classmethod
    def increment_book_count(cls):   # class method count brha raha hai hr dafa new book add honay pr
        cls.total_books += 1


book1 = Book('Python Basic') # one book created
book2 = Book('Machine Learning Basics')

print(Book.total_books)