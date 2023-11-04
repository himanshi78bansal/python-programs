#gcd of two numbers

num1 = int(input("Enter first number : "))
num2 = int(input("Enter first number : "))

def gcd(num1, num2):
    if (num1 == 0):
        return num2
    if (num2 == 0):
        return num1
    if (num1 > num2):
        return gcd(num1-num2, num2)
    return gcd(num1, num2-num1)
(gcd(num1, num2))
print('GCD of', num1, 'and', num2, 'is', gcd(num1, num2))




if (num1<num2):
    for i in range (1,num1+1):
        if(num1%i==0 and num2%i==0):
            gcd=(i)
    print(gcd)
else:
    for i in range (1,num2+1):
        if(num1%i==0 and num2%i==0):
            gcd=(i)
    print(gcd)
    
