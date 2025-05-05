password = str(input("enter password:"))
for i in password:
    if i.isalpha():
        print("it is a letter")
    elif i.isdigit():
        print("it is a number")
    elif i.isspace():
        print("it is a space")
    else:    
        print("it is not a letter, number or space")