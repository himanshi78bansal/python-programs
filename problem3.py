a = [1,6,3,4,5,2,4,5,1,7,3]
b = []
print(a)
for i in a:
    if i not in b:
        b.append(i)
print((b))
