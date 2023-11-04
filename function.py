#Function without parameter
def hello():
    print("Hello World!")
hello()


#Function with parameter
def hello(hi):
    print(hi)
hello("Hello World!")


#Function returning value
def hello(x):
    return x+1
value = (hello(10))
print(value)


#Required keyword function
def data(name,age):
    print("Name is",name,"and age is",age)
data(name="Himanshi Bansal",age = "23")

#Default parameter function
def data(name="Himanshi Bansal",age = "23"):
    print("Name is",name,"and age is",age)

data(name="Himanshi Bansal",age = "24")
data()

#Variable length parameter
#multiple values
def hello(*data):
    print(data)
    print(type(data))
hello(1,2,3,4,5)

#multiple values with key
def hello(**data):
    print(data)
    print(type(data))
hello(a=1,b=2,c=3,d=4,e=5)

#Function inside function
def hello(name,age):
    print("Name : ",name)
    def hi(age):
        print("Age : ",age)
    hi(age)
hello("Himanshi Bansal","23")

#Closure Function
def course(a):
    print("Course : ",a)
    def branch(b):
        print("Branch : ",b)
    return branch
result = course("MCA")
result("CA")

#Lambda Function
hello = lambda a,b:a*b
print(hello(3,7))


a=print
a("hello")

def add(a,b):
    c=a+b
    return c
print(add(5,6))


