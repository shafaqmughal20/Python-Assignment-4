"""
This script generates a random number between 1 and 100 and prompts the user to guess it.
The program provides feedback on whether the guess is too high or too low until the correct random number is guessed.
"""

import random

def main():
    """Handles the game logic for guessing the random number."""
    number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 10 🤔")
    
    guess = int(input("Enter a random guess : "))
    
    while guess != number:
        print("Your guess is too low" if guess < number else "Your guess is too high")
        print()
        guess = int(input("Enter a new guess: "))
    
    print(f"🎉 Congrats! Your random guessed is right. The number was {number}!")

if __name__ == '__main__':
    main()