import random

number = random.randint(1, 100)

guesses = []
attempts = 0

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    guesses.append(guess)
    attempts += 1

    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct Guess")
        break

print("Number of attempts:", attempts)
print("Your guesses:", guesses)