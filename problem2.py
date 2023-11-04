#program to count element of different type of datatype

a=(3,78.7,"hi",8)

intval = 0
floatval = 0
strval = 0

for i in a:
    
    if type(i) == int:
        intval = intval +1
    if type(i) == float:
        floatval = floatval +1
    if type(i) == str:
        strval = strval + 1

print(intval)
print(floatval)
print(strval)
