digit = int(input("Enter a number : "))
sum = 0
while(digit != 0):
    rem = digit%10
    digit = digit-rem
    digit = digit/10
    sum=sum+rem
print(int(sum))
