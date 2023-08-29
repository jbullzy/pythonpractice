# Convert seconds into minutes and seconds

seconds = int(input("How many seconds? >> "))

minutes = (int(seconds / 60))

secondsleft = (int(seconds % 60))

print("Okay, that's {} minutes and {} seconds".format(minutes, secondsleft))

