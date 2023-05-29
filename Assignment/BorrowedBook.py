class BorrowedBook:
    def __init__(self, bid, borrower):
        self.bid = bid
        self.borrower = borrower

def borrow_book(books_list, borrowed_books_list):
    bid = input("Enter the book ID to borrow: ")
    book = books_list.search(bid)

    if book is None:
        print("Book not found in the library.")
    elif book.status == "issued":
        print("Book is already issued to someone.")
    else:
        borrower = input("Enter the borrower name: ")
        book.status = "issued"
        borrowed_book = BorrowedBook(bid, borrower)
        borrowed_books_list.insert(borrowed_book)
        print("Book borrowed successfully.")