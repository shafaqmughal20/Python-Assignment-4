def calculate(mass):
    C = 299792458
    return mass * (C ** 2)

def main():
    '''
    Command line Version of The mass energy calculation 
    '''

    try:
        mass = float(input('Enter Kilogram To Mass :'))
        energy = calculate(mass)

        print('e = m * C^2...')
        print(f'm = {mass} kg')
        print(f'C = {299792458} m/s')
        print(f'e = {energy} Joules of Energy')
    except ValueError:
        print('Invalid input. Please enter a numeric value.')

if __name__ == "__main__":
    main()        