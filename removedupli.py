num = [1,3,2,1,4,3,5,4,5,6,4,7,73,76]
set1 = set()
unique_items = []
for i in num:
    if i not in set1:
        set1.add(i)
        unique_items.append(i)
print(set1)
print(unique_items)