list = [2, 3, 4, 2, 5, 3, 6]
seen = set()
dublicates = set()
for i in list:
    if i not in seen:
        seen.add(i)
    else:
        dublicates.add(i)
print(seen)
print(dublicates)
        