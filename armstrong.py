number = int(input("Enter a 3-digit number : "))
check = number
armstrong = 0
while (number !=0):
    rem = number % 10
    cube = rem**3
    armstrong = armstrong + cube
    number = number // 10
print(armstrong)
if(armstrong == check):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
    
