def view_books(books_list):
    if books_list.is_empty():
        print("No books available in the library.")
    else:
        print("Books in the library:")
        books_list.display()