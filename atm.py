balance = 10000
history = ""

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))

        if amount > balance:
            print("Insufficient Balance")
        else:
            balance = balance - amount
            history = history + "Withdraw ₹" + str(amount) + "\n"
            print("Money Withdrawn Successfully")

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))

        balance = balance + amount
        history = history + "Deposit ₹" + str(amount) + "\n"
        print("Money Deposited Successfully")

    elif choice == 4:
        print("Transaction History")
        if history == "":
            print("No Transactions Yet")
        else:
            print(history)

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")