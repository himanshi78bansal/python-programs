#Swap two numbers

print("Before Swap")
first = int(input("Enter first number : "))
second = int(input("Enter second number : "))

#1st Method
'''
print("After Swap")
print("First number will be : ",second)
print("Second number will be : ",first)
'''

#2nd Method
'''
first,second = second,first
print("First number will be : ",first)
print("Second number will be : ",second)
'''

#3rd Method
'''
temp = first
first = second
second = temp
print("First number will be : ",first)
print("Second number will be : ",second)
'''

#4th Method
first = first+second
second = first-second
first = first-second
print("First number will be : ",first)
print("Second number will be : ",second)




