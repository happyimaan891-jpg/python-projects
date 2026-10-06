import random

def guessing_game():
    print("Welcome to the number guessing game!")
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0
    
    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try higher.")
            elif guess > secret_number:
                print("Too high! Try lower.")
            else:
                print(f"Congratulations! You won. You found it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number!")

guessing_game()

