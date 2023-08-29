def equalto(some_string):
    thestring = some_string
    countx = 0
    county = 0

    for char in thestring:
        if char in 'xX':
            countx += 1

    for char in thestring:
        if char in 'yY':
            county += 1

    print(countx)
    print(county)

    if countx == county: 
        print("Yup, they're equal")
        return True

    elif countx != county:
        print("Nope, not equal")
        return False



xy = input("Enter a string of X's and Y's: ") 

equalto(xy)


        