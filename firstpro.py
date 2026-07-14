library = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    library.append(book)
    print("Book Added Successfully!")

def display_books():
    if not library:
        print("No books available.")
        return

    print("\nLibrary Books:")
    for book in library:
        status = "Issued" if book["issued"] else "Available"
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {status}")

def search_book():
    book_id = input("Enter Book ID to Search: ")
    for book in library:
        if book["id"] == book_id:
            print("Book Found!")
            print(book)
            return
    print("Book Not Found!")

def issue_book():
    book_id = input("Enter Book ID to Issue: ")
    for book in library:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                print("Book Issued Successfully!")
            else:
                print("Book is already issued.")
            return
    print("Book Not Found!")

def return_book():
    book_id = input("Enter Book ID to Return: ")
    for book in library:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                print("Book Returned Successfully!")
            else:
                print("Book was not issued.")
            return
    print("Book Not Found!")

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Please try again.")