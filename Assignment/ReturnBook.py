def return_book(books_list, borrowed_books_list):
    bid = input("Enter the book ID to return: ")
    borrowed_books_list.delete(bid)
    book = books_list.search(bid)

    if book is not None:
        book.status = "available"
        print("Book returned successfully.") 
    else: 
        print("Book not found in the borrowed books list.")