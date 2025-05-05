import math

n = int(input("Enter number: "))

if n <= 1:
    print("Not prime")
elif n == 2:
    print("Prime")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not prime")
 