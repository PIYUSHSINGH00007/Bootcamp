# Create and Write to a File

# Open the file in write mode
file = open("student.txt", "w")

# Accept text input from the user
text = input("Enter text to store in the file: ")

# Write the text to the file
file.write(text)

# Close the file
file.close()

# Display success message
print("Data written successfully to student.txt")