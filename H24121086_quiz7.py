library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here

    book = input("Enter the title, genre, and price of the book (separated by |): ")
    book = book.split("|")
    title = ''.join(book[0])
    genre = ''.join(book[1])
    price = ''.join(book[2])
    library[title] = [genre, price]

    print("Added", title, "to the library.\n")


def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here

    book_remove = input("Enter the title of the book to remove: ")

    if book_remove in library:
        del library[book_remove]
        print("Book removed.")
        return True
    else:
        print("Error:", book_remove, "not found in the library.")
        return False


def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here

    book_info = input("Enter the title fo the book: ")

    if book_info in library:
        print("Title: ", book_info,"\nGenre: ", library[book_info[0]], "\nPrice: ", library[book_info[1]])
        return True
    else:
        print("Error: ", book_info, "not fond in the library.")
        return False


def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here

    for key in sorted(library.keys()):
        print("%s (%s, $%.2f)" % (title, genre, price))

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

