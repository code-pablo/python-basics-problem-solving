import math
num = int(input("Enter a number: "))
sum = 0
temp = str(num)
power = len(temp)
for i in temp:
    sum += int(i)**power
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")