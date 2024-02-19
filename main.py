class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book}'.")
        else:
            print(f"{self.name} didn't borrow '{book}'.")


class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename

    def close_file(self):
        self.file.close()

    def list_books(self):
        with open(self.filename, "r") as file:
            books = file.readlines()
            if not books:
                print("No books available.")
                return

            print("List of Books:")
            for book in books:
                book_info = book.strip().split(",")
                if len(book_info) == 4:
                    print(
                        f"Title: {book_info[0]}, Author: {book_info[1]}, Release Date: {book_info[2]}, Pages: {book_info[3]}")
                else:
                    print("Invalid book entry:", book)

    def add_book(self):
        with open(self.filename, "a") as file:
            book_info = input("Enter book information (title, author, release date, pages), separated by commas: ")
            file.write(book_info + "\n")
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ").strip().lower()
        with open(self.filename, "r") as file:
            books = file.readlines()

        updated_books = []
        removed = False
        for book in books:
            if title not in book.lower():
                updated_books.append(book)

        if len(updated_books) == len(books):
            print("Book not found.")
            return

        with open(self.filename, "w") as file:
            file.writelines(updated_books)
        print("Book removed successfully.")

    def borrow_book(self, user):
        title = input("Enter the title of the book to borrow: ").strip().lower()
        with open(self.filename, "r") as file:
            books = file.readlines()

        for book in books:
            book_info = book.strip().split(",")
            if title == book_info[0].lower():
                user.borrow_book(book_info[0])
                self.remove_book(title)
                return

        print("Book not available.")

    def return_book(self, user):
        title = input("Enter the title of the book to return: ").strip().lower()
        if title in user.borrowed_books:
            user.return_book(title)
            with open(self.filename, "a") as file:
                file.write(title + "\n")
        else:
            print(f"You haven't borrowed '{title}'.")


# Create Library object
lib = Library()

# Create User object
user = User("John")

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Borrow Book")
    print("5) Return Book")
    print("6) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.borrow_book(user)
    elif choice == "5":
        lib.return_book(user)
    elif choice == "6":
        lib.close_file()
        break
    else:
        print("Invalid choice. Please enter a valid option.")
