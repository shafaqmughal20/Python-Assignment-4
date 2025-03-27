import random  # Importing random module to let the computer make a choice

def get_computer_choice():
    """Returns a random choice for the computer (rock, paper, or scissors)."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    """Determines the winner based on game rules."""
    if user == computer:
        return "🤝 It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "🎉 You win!"
    else:
        return "💀 You lose!"

def play_game():
    """Main function to play Rock, Paper, Scissors."""
    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    # Get user input
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please enter rock, paper, or scissors.")
        return

    # Get computer's choice
    computer_choice = get_computer_choice()

    # Display choices
    print(f"\n🧑 You chose: {user_choice}")
    print(f"🤖 Computer chose: {computer_choice}")

    # Determine and display winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
play_game()
