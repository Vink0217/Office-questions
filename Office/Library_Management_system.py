'''
Q16) Library Management System 
Create classes for Book and Library. Add methods to borrow and return books. 
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        if self.is_borrowed:
            Book_available = "Borrowed"
        else:
            Book_available = "Available"
    
        return f"'{self.title}' by {self.author} - {Book_available}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Collection: ")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"\n You borrowed '{book.title}'")
                return
        print(f"\n'{title}' is not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"\nYou returned '{book.title}'")
                return
        print(f"\n'{title}' was not borrowed from this library.")

if __name__ == "__main__":
    library = Library()

    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

    choice = int(input("What do you wanna do? \n 1.Display the books. \n 2.Borrow a book. \n 3.Return a Book \n Choose your option: "))
    if choice == 1:
        library.display_books()
    elif choice == 2:
        book_title = str(input("Enter the Name or the Author of the Book: "))
        library.borrow_book(book_title)
        library.display_books()
    elif choice == 3:
        book_title = str(input("Enter the Name or the Author of the Book: "))
        library.return_book(book_title)
        library.display_books()
    else:
        print("Wrong Input")

    
    
