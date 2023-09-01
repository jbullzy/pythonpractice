counts = dict()
names = ['john', 'jack', 'tom', 'mike', 'ashley']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)