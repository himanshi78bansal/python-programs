n = int(input("Enter the n which are looking square root"))
x = int (input("Enter the value of x"))
approx = 0.5*n
for i in range (x):
    sqr = 0.5*(approx + n/approx)
    approx = sqr
print(sqr)
