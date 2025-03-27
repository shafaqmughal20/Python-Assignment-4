Inches_in_foot : int = 12


def main():
    '''
    Command Line interface of Feet to inches Converter
    '''

    try:
        feet = float(input("Enter the number of feet: "))
        inches = feet * Inches_in_foot
        print(f"{feet} feet is equal to {inches} inches.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        

if __name__ == "__main__":
 main()        