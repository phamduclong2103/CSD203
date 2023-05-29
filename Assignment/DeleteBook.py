def delete_book(books_list):
    bid = input("Enter the book ID to delete: ")
    books_list.delete(bid)
    print("Book deleted successfully.")