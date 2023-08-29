def creditcard():
    number = input("Enter your credit card number: ")

    first_numbers = len(number) - 4

    hiddennumber = '*' * first_numbers + number[:4]

    print(hiddennumber)

creditcard()