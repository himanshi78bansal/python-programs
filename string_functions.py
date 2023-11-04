a = "Hello"
b = "1115656565hgjhghj"
c = "hello, namaste, hello"

#upper()
print(a.upper())

#upper()
if b.isupper():
    print("True")
else:
    print("False")
    
#lower()
print(a.lower())

#lower()
if a.islower():
    print("True")
else:
    print("False")

#startswith()
print(c.startswith("hello"))
    
#startswith
if a.startswith("Hello"):
    print("True")
else:
    print("False")

#endswith()
print(c.endswith("hello"))

#endswith    
if b.endswith("Hello"):
    print("True")
else:
    print("False")

#isalpha()
if a.isalpha():
    print("true")
else:
    print("false")

#isnum()
if b.isalnum():
    print("true")
else:
    print("false")

#isalnum()
print(c.isalnum())

#isspace()
if b.isspace():
    print("true")
else:
    print("false")

#length()
print(len(a))

#count()
print(a.count("H"))

#find()
print(c.find("Llo"))

#rfind()
print(c.rfind("llox"))

#strip()
print(a.strip('-'))

#lstrip()
print(a.lstrip('-'))

#rstrip()
print(a.rstrip('-'))

#index()
print(c.index("lo"))

#rindex()
print(c.rindex("lo"))

#split
print(a.split("e"))

#join
print("#".join(a))

#replace
print(a.replace("Hello","Hi"))

#Capitalize
print(c.capitalize())

#rjust
print(a.rjust(10,"#"))

#ljust
print(a.ljust(10,"#"))

#partition
print(a.partition("l"))

#zfill
print(a.zfill(10))

#format
print(("Hello {}").format("World"))

#hash
print(hash(a))
