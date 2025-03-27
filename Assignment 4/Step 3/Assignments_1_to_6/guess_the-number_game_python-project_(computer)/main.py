import random  # Importing random module to generate a random number

def number_guessing_game():
    """This function runs a number guessing game."""
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Counter for number of attempts

    while True:  # Infinite loop until the user guesses correctly
        try:
            guess = int(input("Enter your guess: "))  # Take user input as an integer
            attempts += 1  # Increment attempt count

            if guess < 1 or guess > 100:  # Check if guess is out of range
                print("🚨 Please enter a number between 1 and 100.")
                continue  # Skip to the next iteration

            if guess < secret_number:
                print("📉 Too low! Try again.")  # Hint: Guess a higher number
            elif guess > secret_number:
                print("📈 Too high! Try again.")  # Hint: Guess a lower number
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break  # Exit the loop when the correct number is guessed

        except ValueError:  # Handle invalid input (non-integer)
            print("❌ Invalid input! Please enter a valid number.")

# Run the game
number_guessing_game()
