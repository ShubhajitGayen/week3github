class Book:
    """Represents an individual book asset within the library catalog."""
    
    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_issued = False  # Operational availability flag

    def __str__(self) -> str:
        status = "Issued" if self.is_issued else "Available"
        return f"ISBN: {self.isbn} | Title: '{self.title}' | Author: {self.author} | [{status}]"


class Library:
    """Manages collection inventories and circulation operations."""
    
    def __init__(self, name: str):
        self.name = name
        self.__books = {}  # Encapsulated collection store: {isbn: Book_Object}

    def add_book(self, book: Book) -> str:
        """Adds a new Book instance to the system storage map."""
        if book.isbn in self.__books:
            return f"Operation Failed: Book with ISBN {book.isbn} already exists."
        
        self.__books[book.isbn] = book
        return f"Success: '{book.title}' added to {self.name} inventory."

    def remove_book(self, isbn: str) -> str:
        """Removes a target Book instance via its unique ISBN key index."""
        if isbn not in self.__books:
            return f"Operation Failed: ISBN {isbn} not found in catalog."
        
        removed_book = self.__books.pop(isbn)
        return f"Success: '{removed_book.title}' permanently removed."

    def issue_book(self, isbn: str) -> str:
        """Transitions book status to issued if found and currently available."""
        if isbn not in self.__books:
            return "Operation Failed: Book asset matching requested identifier does not exist."
        
        book = self.__books[isbn]
        if book.is_issued:
            return f"Conflict: '{book.title}' is already checked out."
        
        book.is_issued = True
        return f"Success: '{book.title}' has been successfully issued."

    def return_book(self, isbn: str) -> str:
        """Reclaims an issued book asset, resetting its available flag state."""
        if isbn not in self.__books:
            return "Operation Failed: Asset lookup error during return processing."
        
        book = self.__books[isbn]
        if not book.is_issued:
            return f"Error: '{book.title}' was not flagged as issued in this system."
        
        book.is_issued = False
        return f"Success: '{book.title}' safely returned to shelves."

    def display_available_books(self) -> None:
        """Iterates collection map and logs properties of items not issued."""
        print(f"\n--- Available Books in {self.name} ---")
        available_books = [b for b in self.__books.values() if not b.is_issued]
        
        if not available_books:
            print("No books are currently available for loan.")
            return
            
        for book in available_books:
            print(book)
        print("-" * 40)


# =====================================================================
# SYSTEM VERIFICATION AND OPERATIONAL TESTING BLOCK
# =====================================================================
if __name__ == "__main__":
    # 1. Initialize our Library Management Domain
    my_library = Library("City Central Library")

    # 2. Instantiate Book Entities
    b1 = Book("978-0141439518", "Pride and Prejudice", "Jane Austen")
    b2 = Book("978-0451524935", "1884", "George Orwell")
    b3 = Book("978-0316769488", "The Catcher in the Rye", "J.D. Salinger")

    print("--- 1. Testing Book Addition ---")
    print(my_library.add_book(b1))
    print(my_library.add_book(b2))
    print(my_library.add_book(b3))

    # 3. View Inventory
    my_library.display_available_books()

    print("\n--- 2. Testing Circulation (Issuing) ---")
    print(my_library.issue_book("978-0451524935"))  # Valid transaction
    print(my_library.issue_book("978-0451524935"))  # Test redundancy conflict exception

    # 4. View Inventory after structural update
    my_library.display_available_books()

    print("\n--- 3. Testing Returns & Purges ---")
    print(my_library.return_book("978-0451524935")) # Safe return
    print(my_library.remove_book("978-0316769488")) # Complete removal from database

    # Final Inventory Evaluation State
    my_library.display_available_books()
