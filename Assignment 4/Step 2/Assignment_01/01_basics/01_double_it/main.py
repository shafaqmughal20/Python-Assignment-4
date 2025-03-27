"""
This script takes a user input number and continuously doubles it 
until it reaches or exceeds 100, printing each intermediate value.
"""

def main():
    """Gets user input and doubles it in a loop until it reaches 100 or more."""
    curr_value = int(input("Enter a number: "))
    
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")
    
    print("\nProcess complete!")

if __name__ == '__main__':
    main()
