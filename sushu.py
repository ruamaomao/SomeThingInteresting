l = []
for x in range(100):
    if x <2:
        continue
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        l.append(x)
print(l)
#  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
