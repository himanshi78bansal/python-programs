'''
sum=0
i=0
print("i j sum ")
while(i<10):
    for j in range(5):
        if(i>j):
            continue
        sum+=j
        print(i,j,sum)
        if(j==3):
            break
    i=i+2
print("last = ",sum)





sum=0
for i in range(100):
    if((i%2==0)or(i%3==0)):
        continue
    if(i%5==0)and(i%7==0):
        break
    sum=sum+i
print("sum ",sum)
'''
text=5
no=6
print('{name} has {age} this'.format(name=text,age=no))



#homework
#list comprehension
#type of function
