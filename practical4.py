a = []
print("Input list")
for i in range (1,6):
    n = int(input())
    a.append(n)
print(a)
n = int(input("Enter the number you want the location : "))
c = 0
for i in range (len(a)):
    if (n == a[i]):
        c = i+1
        break
print("location : ",c)
