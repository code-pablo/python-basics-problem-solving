word = str(input("enter a word")).lower()
vowels = ["a","e","i","o","u"]
total_vowels = 0
for i in word:
    if i in vowels:
        total_vowels += 1
if total_vowels == 0:    
    print("no vowels")
else:    
    print("there are",total_vowels,"vowels")
