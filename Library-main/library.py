class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You have borrowed '{title}'.")
                return
        print(f"Sorry, '{title}' is not available or does not exist in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                print(f"Thank you for returning '{title}'.")
                return
        print(f"'{title}' was not borrowed from this library or does not exist in the library.")

    def display_books(self):
        print("\nLibrary Collection:")
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)
        print()

def main():
    library = Library()

    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)
        
        elif choice == "2":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        
        elif choice == "3":
            title = input("Enter book title to return: ")
            library.return_book(title)
        
        elif choice == "4":
            library.display_books()
        
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
