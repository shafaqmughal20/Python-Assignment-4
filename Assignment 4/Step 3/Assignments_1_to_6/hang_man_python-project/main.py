import random  # Importing random module to select a random word

def choose_word():
    """Returns a random word from the list."""
    words = ["python", "hangman", "developer", "programming", "challenge", "project"]
    return random.choice(words)  # Select a random word from the list

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and unguessed letters as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    """Main function to run the Hangman game."""
    print("🎯 Welcome to Hangman!")
    secret_word = choose_word()  # Choose a random word
    guessed_letters = set()  # Set to store correctly guessed letters
    attempts = 6  # Player has 6 chances before losing
    
    while attempts > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))  # Show the word progress
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Enter a letter: ").lower()  # Get user input and convert to lowercase
        
        if len(guess) != 1 or not guess.isalpha():  # Ensure input is a single letter
            print("❌ Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:  # Check if the letter was already guessed
            print("⚠️ You already guessed this letter!")
            continue

        guessed_letters.add(guess)  # Add the guessed letter to the set
        
        if guess in secret_word:  # Check if the guessed letter is in the secret word
            print("✅ Correct guess!")
        else:
            print("❌ Incorrect guess!")
            attempts -= 1  # Reduce attempts if the guess is incorrect
        
        if all(letter in guessed_letters for letter in secret_word):  # Check if word is completely guessed
            print(f"🎉 Congratulations! You guessed the word: {secret_word}")
            break
    else:
        print(f"💀 Game Over! The correct word was: {secret_word}")

# Run the Hangman game
hangman()
