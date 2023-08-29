# Sorting a list in Python

def thelist(mylist, myorder):

    print("Here's your list: ")
    print(mylist)

    sorted_list = sorted(mylist)
    reverse_sorted_list = sorted(mylist, reverse=True)

    if myorder == "asc": 
        print("Okay, here's the ascending list: ")
        print(sorted_list)
        
    elif myorder == "desc":
        print("Okay, here's the descending list: ")
        print(reverse_sorted_list)

    else: 
        print("Invalid input. Enter 'asc' or 'desc'")
 


user_list = input("Enter the list elements separated by spaces: ")
user_order = input("How do you want your list sorted? >> ")

mylist = [int(item) for item in user_list.split()]

thelist(mylist, user_order)