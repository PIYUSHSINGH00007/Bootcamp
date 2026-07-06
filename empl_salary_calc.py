# Employee Salary Calculator

employees = []

while True:
    print("\n===== Employee Salary Calculator =====")
    print("1. Add Employee")
    print("2. View Employee Details")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))

        hra = basic * 0.20
        da = basic * 0.10
        gross = basic + hra + da

        employee = [name, basic, hra, da, gross]
        employees.append(employee)

        print("Employee details added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\n----- Employee Salary Details -----")
            for emp in employees:
                print("\nEmployee Name :", emp[0])
                print("Basic Salary  :", emp[1])
                print("HRA (20%)     :", emp[2])
                print("DA (10%)      :", emp[3])
                print("Gross Salary  :", emp[4])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")