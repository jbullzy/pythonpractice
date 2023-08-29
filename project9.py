# Calculator function that accepts three variables: 

def calculator(int1, operator, int2):
    if operator == "+":
        return int1 + int2
    elif operator == "-":
        return int1 - int2
    elif operator == "*":
        return int1 * int2
    elif operator == "/":
        if int2 != 0:
            return int1 / int2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"


firstinteger = int(input("Enter the first integer: "))
operator = input("Enter the Operator: ")
secondinteger = int(input("Enter the second integer: "))

result = calculator(firstinteger, operator , secondinteger)
print(result)