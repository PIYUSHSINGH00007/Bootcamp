# Set Operations Program

# Taking input for Set A
set_a = set(map(int, input("Enter elements of Set A (space-separated): ").split()))

# Taking input for Set B
set_b = set(map(int, input("Enter elements of Set B (space-separated): ").split()))

# Display sets
print("\nSet A:", set_a)
print("Set B:", set_b)

# Union
print("Union:", set_a.union(set_b))

# Intersection
print("Intersection:", set_a.intersection(set_b))

# Difference (A - B)
print("Difference (A-B):", set_a.difference(set_b))

# Symmetric Difference
print("Symmetric Difference:", set_a.symmetric_difference(set_b))

# Remove duplicates from a list
numbers = list(map(int, input("\nEnter list elements (space-separated): ").split()))

unique_numbers = list(set(numbers))

print("List after removing duplicates:", unique_numbers)