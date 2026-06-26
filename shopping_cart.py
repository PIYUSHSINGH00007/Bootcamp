products = []

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. View Products")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        p = input("Enter product name: ")
        products.append(p)
        print("Product added.")

    elif choice == "2":
        p = input("Enter product name to remove: ")
        if p in products:
            products.remove(p)
            print("Product removed.")
        else:
            print("Product not found.")

    elif choice == "3":
        print("Products:")
        for i in products:
            print(i)
        print("Total products:", len(products))

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Wrong choice.")