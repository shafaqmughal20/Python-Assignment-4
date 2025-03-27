def mad_libs():
    """This function runs a simple Mad Libs game where users input words to complete a story."""
    
    print("🎭 Welcome to the Mad Libs Game!")
    print("Fill in the blanks with the required words.\n")

    # Asking user for different types of words
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

    # Creating a Mad Libs story with the user's words
    story = f"""
    One day, a {adjective} {noun} decided to {verb} all the way to {place}.
    Everyone was surprised to see such a sight!
    It became the most talked-about event in the entire town.
    """

    # Displaying the completed story
    print("\n🎉 Here is your Mad Libs story:")
    print(story)

# Run the Mad Libs game
mad_libs()
