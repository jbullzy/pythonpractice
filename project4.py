# Sorting a list in Python. This one returns to the top on invalid input. 

def thelist(mylist, myorder):

    print("Here's your list: ")
    print(mylist)

    sorted_list = sorted(mylist)
    reverse_sorted_list = sorted(mylist, reverse=True)

    if myorder == "asc": 
        print("Okay, here's the ascending list: ")
        print(sorted_list)
        return False
        
    elif myorder == "desc":
        print("Okay, here's the descending list: ")
        print(reverse_sorted_list)
        return False

    else: 
        print("Invalid input. Enter 'asc' or 'desc'")
        return True
 

user_list = input("Enter the list elements separated by spaces: ")

# This part verifies that it's only numbers entered in by the user.
try:
    mylist = [int(item) for item in user_list.split()]
except ValueError:
    print("Invalid input. Please enter only numbers separated by spaces.")
    exit(1)

# This part verifies the user entering in only 'asc' or 'desc'
while True:
    user_order = input("How do you want your list sorted? >> ")
    if not thelist(mylist, user_order):
        break 

thelist(mylist, user_order)