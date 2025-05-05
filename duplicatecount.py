num = [1,3,2,4,2,3,4,5,6,3,4,2,7,6,8,6,8,]
freq = {}
for i in num:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)