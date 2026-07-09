# Student Marks Analyzer Using List

marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

print("\nHighest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))

# Ascending Order
marks.sort()
print("Ascending Order:", marks)

# Descending Order
marks.sort(reverse=True)
print("Descending Order:", marks)

# Search for a mark
search = int(input("\nEnter mark to search: "))

if search in marks:
    print("Mark found.")
else:
    print("Mark not found.")