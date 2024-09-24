import random

# Randomly selects a number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
user_guess = None

print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100. Can you guess it?")

# Loop until the user guesses the correct number
while user_guess != secret_number:
    user_guess = int(input("Enter your guess: "))
    attempts += 1
    
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")

print("Thanks for playing!")
