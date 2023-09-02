# Initializes the dictionary 'd'
d = dict()
# Adds the key 'csev' with the value '2'. Likewise with the next line. 
d['csev'] = 2
d['cwen'] = 4

print(d.items())

# for (tupled variables k and v) in the dictionary 'd' (.items puts them in a format dict_items([('csev',2), ('cwen',4)]))
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)