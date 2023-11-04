print("\n1 for add\n2 for sub\n3 for div\n4 for mul\n")
choice = int(input("Enter a choice--"))

x = int(input("Enter first value : "))
y = int(input("Enter first value : "))

if(choice==1):
    print(x+y)
elif(choice==2):
    print(x-y)
elif(choice==3):
    print(x/y)
elif(choice==4):
    print(x*y)
