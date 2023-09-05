import re

hand = open('project36.py')
for line in hand:
    line = line.rstrip()
    # Searches the line for 'for' the ^ carat is a regular expression that indicates that only 
    # Lines that BEGIN with for are being searched for.
    if re.search('^for', line) :
        print(line)