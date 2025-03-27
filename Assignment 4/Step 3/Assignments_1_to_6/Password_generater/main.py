import random  # Importing random module to generate random characters
import string  # Importing string module to get letters, digits, and symbols

def generate_password(length):
    """This function generates a random password of a given length."""
    
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password  # Return the generated password

# Ask user for password length
try:
    length = int(input("🔐 Enter the desired password length: "))
    if length < 4:
        print("⚠️ Password should be at least 4 characters long!")
    else:
        generated_password = generate_password(length)
        print(f"\n✅ Your Secure Password: {generated_password}")

except ValueError:
    print("❌ Invalid input! Please enter a valid number.")
