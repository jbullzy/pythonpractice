# Converting a decimal number to binary

def convert_binary(number):
    if number == 0:
        return '0b0'

    binary_representation = ''
    while number > 0:
        remainder = number % 2
        binary_representation = str(remainder) + binary_representation
        number //= 2

    return '0b' + binary_representation 

number = int(input("Enter a number: "))

binary_number = convert_binary(number)

print(f"The binary representation of {number} is {binary_number}")