c = {'a':10, 'b':1, 'c':22}


# This is a condensed version of the sorting dictionary algorith we made in the earlier projects. 
# Prints the contents.
# Sorts the contents.
# [] denotes a list or dictionary. In this case it's a list we're creating in there.
# Tuple (v,k) is the 'format' were making the list in. For k,v in the dictionary c. 
# For example, 'a':10 is the first item out of the list. It takes 'a' as 'k' and '10' as 'v', then stores them as v,k
# All the elements in the dictionary are run through without having to store them in a variable. 
print(sorted([(v,k) for k,v in c.items()]))