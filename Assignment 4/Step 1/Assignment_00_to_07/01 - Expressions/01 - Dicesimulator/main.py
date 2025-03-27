import random

Num_Sides=6


def roll():
    '''
    Simulates and rolling Two Dice And Prints thier Total Numbers
    '''

    roll1 = random.randint(1, Num_Sides)
    roll2 = random.randint(1, Num_Sides)
    total = roll1 + roll2
    print(f'You rolled a {roll1} and a {roll2}. The total is {total}.')

def main():
    roll1 = 10 

    print(f'Roll 1 is main Starts As :{roll1}')    


    for i in range(3):
        roll()

        print(f'Roll 2 is main Starts As :{roll1}')

if __name__ == '__main__':
    main()        