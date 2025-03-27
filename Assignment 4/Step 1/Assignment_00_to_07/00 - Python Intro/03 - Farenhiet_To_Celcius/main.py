def main():
    farenhiet = float(input('Enter Your Temperature In Farenhiet :'))

    celsius = (farenhiet - 32) * 5/9

    print(f'Your Temperature In Celsius Is : {celsius}')

if __name__ == '__main__':
    main()    