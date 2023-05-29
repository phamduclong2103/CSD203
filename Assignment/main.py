from LinkedList import LinkedList
from AddBook import add_book
from ViewBooks import view_books
from DeleteBook import delete_book
from BorrowedBook import borrow_book
from ReturnBook import return_book

def display_menu():
    print("Library Management System Menu:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("0. Exit")

def run():
    books_list = LinkedList()
    borrowed_books_list = LinkedList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books_list)
        elif choice == '2':
            view_books(books_list)
        elif choice == '3':
            delete_book(books_list)
        elif choice == '4':
            borrow_book(books_list, borrowed_books_list)
        elif choice == '5':
            return_book(books_list, borrowed_books_list)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()