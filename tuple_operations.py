# Create a tuple of five integers
numbers = (10, 20, 30, 40, 50)

# Display the tuple
print("Tuple:", numbers)

# Display length
print("Length of tuple:", len(numbers))

# Display maximum value
print("Maximum value:", max(numbers))

# Display minimum value
print("Minimum value:", min(numbers))

# Display sum of all elements
print("Sum of elements:", sum(numbers))

# Search for an element
element = int(input("Enter element to search: "))

if element in numbers:
    print("Element found in tuple.")
else:
    print("Element not found in tuple.")