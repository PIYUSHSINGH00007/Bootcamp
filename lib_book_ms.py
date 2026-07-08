# Library Book Management System

books = []

while True:
    print("\n===== Library Book Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Total Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        book = input("Enter book name to remove: ")

        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found!")

    elif choice == "3":
        book = input("Enter book name to search: ")

        if book in books:
            print("Book is available in the library.")
        else:
            print("Book is not available.")

    elif choice == "4":
        if len(books) == 0:
            print("No books in the library.")
        else:
            print("\nBooks Available:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])

    elif choice == "5":
        print("Total books available:", len(books))

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")