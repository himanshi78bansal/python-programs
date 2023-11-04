num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
result = num1
print(num1**num2)

for i in range (num2-1):
    result = result*num1
print(result)



