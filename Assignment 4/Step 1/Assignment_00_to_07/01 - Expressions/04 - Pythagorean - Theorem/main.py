import math


def main():
    '''

    command line version of the pythegoren theorem calculator
    '''

    try:
        a = float(input('Enter the Length of the first side : '))
        b = float(input('Enter the Length of the second side : '))

        c = math.sqrt(a **2 + b **2)

        print(f'The length of the third side bc (Hypotenuese) is {c}')

    except ValueError:
        print('Enter a number Valid Number: {0}'.format())



if __name__ == "__main__":
    main()