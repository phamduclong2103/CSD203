class Book:
    def __init__(self, bid, title, author, status):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status

def add_book(books_list):
    bid = input("Enter the book ID: ")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    status = "available"
    book = Book(bid, title, author, status)
    books_list.insert(book)
    print("Book added successfully.")