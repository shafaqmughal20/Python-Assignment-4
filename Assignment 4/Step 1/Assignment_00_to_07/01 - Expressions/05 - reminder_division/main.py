def main():
    '''
    command line version of division calculator

    '''
try:
    divide = int(input('Plz Enter A Intiger To divided :'))

    divisor = int(input('Plz Enter A Intiger To Divided By :'))


    if divisor == 0 :
        print('Error : Division by zero is not allowed.')
        quit()
    
    quitent = divide // divisor
    remainder = divide % divisor

    print(f'The Result Of This Division is : {quitent} With The remainder : {remainder}')

except ValueError:
    print('Error : Please Enter A Valid Intiger')

except ZeroDivisionError:
    print('Error : Division by zero is not allowed.')

if __name__ == '__main__':
    main()    