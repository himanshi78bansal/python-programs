'''
name = str(input("Enter your name : "))
print(name)
n=5
split = name.split()[:5]
print(split)

for(i!=0):
    word = split[i]
    capital = word.capitalize()
    print(capital)
'''

'''
a=('1','2','3','4','5','6')
print(a[4:-1:-1])
'''

string = input("Enter a string")

acc = ""

for char in string:

    if char in "'.,;:?! ":

        char = string.upper()

        acc +=  char

print(acc)
