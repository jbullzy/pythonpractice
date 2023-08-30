xfile = open('project19.py')
inp = xfile.read()

print(len(inp))


count = 0
for line in xfile:
    if 'banana' in line:
        count = count + 1

print(count)