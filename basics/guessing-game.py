import random

print("=== Number Guessing Game ===")

# Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

# Allow user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check guess
if guess == secret_number:
    print("Correct! You guessed the number!")
else:
    print(f"Wrong guess! The correct number was {secret_number}.")
