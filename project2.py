seconds = int(input("How many seconds? >> "))

minutes, secondsleft = divmod(seconds, 60)

print("That's {} minutes and {} seconds.".format(minutes, secondsleft))