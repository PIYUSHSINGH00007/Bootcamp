marks = []

for i in range(5):
    mark = int(input("Enter marks of subject " + str(i + 1) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

highest = max(marks)
lowest = min(marks)

print("\n----- Student Result -----")
print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)