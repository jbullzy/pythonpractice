jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))

print("Printing keys: ")
print(jjj.keys())

print("Printing values: ")
print(jjj.values())

print("Printing items: ")
print(jjj.items())

for aaa,bbb in jjj.items():
    print(aaa, bbb)