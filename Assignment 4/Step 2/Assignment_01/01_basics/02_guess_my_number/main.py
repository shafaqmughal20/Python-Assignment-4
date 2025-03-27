"""
This script generates a random number between 1 and 99 and prompts the user to guess it.
The program provides feedback on whether the guess is too high or too low until the correct number is guessed.
"""

import random

def main():
    """Handles the game logic for guessing the random number."""
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")
    
    guess = int(input("Enter a guess: "))
    
    while guess != secret_number:
        print("Your guess is too low" if guess < secret_number else "Your guess is too high")
        print()
        guess = int(input("Enter a new guess: "))
    
    print(f"🎉 Congrats! You guessed it right. The number was {secret_number}!")

if __name__ == '__main__':
    main()