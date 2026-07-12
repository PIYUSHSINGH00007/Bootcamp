# Dictionary-Based Student Database

students = {}

while True:
    print("\n----- Student Database -----")
    print("1. Add Student")
    print("2. Update Student Marks")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))
            students[roll] = {"Name": name, "Marks": marks}
            print("Student added successfully.")

    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            marks = int(input("Enter New Marks: "))
            students[roll]["Marks"] = marks
            print("Marks updated successfully.")
        else:
            print("Student not found!")

    elif choice == "3":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Roll Number:", roll)
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found!")

    elif choice == "4":
        roll = input("Enter Roll Number: ")

        if roll in students:
            del students[roll]
            print("Student record deleted.")
        else:
            print("Student not found!")

    elif choice == "5":
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for roll, details in students.items():
                print("Roll Number:", roll)
                print("Name:", details["Name"])
                print("Marks:", details["Marks"])
                print("----------------------")

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")