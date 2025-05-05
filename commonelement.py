list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
#for i in list1:
   # if i in list2:
    #    print(i)
   # else:
   #  print("not found")
list1 = set(list1)
list2 = set(list2)
print(list1.intersection(list2))