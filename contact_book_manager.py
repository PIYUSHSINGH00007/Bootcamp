# Simple Contact Book

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print("Name :", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for name, number in contacts.items():
                print(name, "-", number)

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")