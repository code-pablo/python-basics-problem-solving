word = str(input("enter a word")).strip().lower()
reverse = ""
for i in word:
  reverse = i + reverse
if reverse == word:
    print("it is a palindrome")
else:
    print("it is not a palindrome")