digit = int(input("Enter a number : "))
temp=digit
reverse = 0
while(digit != 0):
    rem = digit % 10
    reverse = (reverse * 10) + rem
    digit = digit // 10
print(reverse)
if (temp == reverse):
    print("digit is palindrome")
else:
    print("digit is not palindrome")
