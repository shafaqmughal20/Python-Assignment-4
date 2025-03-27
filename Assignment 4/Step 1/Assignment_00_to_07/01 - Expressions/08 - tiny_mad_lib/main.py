# Sentence starter
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    """Prompts the user for an adjective, noun, and verb to create a fun sentence."""
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Print the final sentence
    print(SENTENCE_START + f"{adjective} {noun} {verb}!")

if __name__ == "__main__":
    main()