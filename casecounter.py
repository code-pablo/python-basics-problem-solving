word = str(input("enter a word"))
symbol = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",":",";","'","\"",",",".","/","?","<",">","`","~"]
symbol_count = 0
upper_count = 0
lower_count = 0
digit_count = 0
for i in word:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1
    if i.isdigit():
        digit_count += 1
    elif i in symbol:
         symbol_count += 1


print("upper case:",upper_count)
print("lower case:",lower_count)
print("digit:",digit_count)
print("symbol:",symbol_count)