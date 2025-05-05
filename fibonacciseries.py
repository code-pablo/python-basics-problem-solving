n = int(input("entar number of terms:"))
a = 0
b = 1
c= 0
for i in range(n):
   print(a, end=" ")
   c = a + b
   a = b
   b = c
   
