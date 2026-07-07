# Vowel and Consonant Counter

text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in text:
    if ch == " ":
        continue
    elif ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("\n----- Result -----")
print("Vowels            :", vowels)
print("Consonants        :", consonants)
print("Digits            :", digits)
print("Special Characters:", special)