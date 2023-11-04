#Operators.py

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

#arithmetic operators
sum=num1+num2
sub=num1-num2
floatDiv=num1/num2
floorDiv=num1//num2
mul=num1*num2
power=num1**num2
mod=num1%num2

print("sum = ",sum ,"\n")
print("sub = ",sub ,"\n")
print("floatDiv = ",floatDiv ,"\n")
print("floorDiv = ",floorDiv ,"\n")
print("mul = ",mul ,"\n")
print("power = ",power ,"\n")
print("mod = ",mod ,"\n")

#comparison operators
print("Greater ",num1>num2 ,"\n")
print("Lesser ",num1<num2 ,"\n")
print("Equals ",num1==num2 ,"\n")
print("Not Equals ",num1!=num2 ,"\n")
print("Greater than or Equals to ",num1>=num2 ,"\n")
print("Smaller than or Equals to ",num1<=num2 ,"\n")

#logical and bitwise operators
print("and = ",num1 & num2 ,"\n")
print("or = ", num1 | num2 ,"\n")
print("not = ", ~ num1 ,"\n")
print("right shift = ",num1 >> num2 ,"\n")
print("left shift = ", num1 << num2 ,"\n")

#Assignment operators

temp=num1
print("Assign = ",temp ,"\n")
temp+=num1
print("Add & Assign = ", temp ,"\n")
temp//=num1
print("floor divide & Assign = ", temp ,"\n")
temp**=num2
print("Exp & Asssign = ",temp,"\n")



