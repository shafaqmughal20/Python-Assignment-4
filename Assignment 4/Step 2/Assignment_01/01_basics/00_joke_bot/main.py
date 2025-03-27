PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Why did the developer go broke? Because he used up all his cache!"
SORRY = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT).strip().lower()
    print(JOKE if user_input == "joke" else SORRY)

if __name__ == "__main__":
    main()
