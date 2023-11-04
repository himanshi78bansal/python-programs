file = open("file.txt","r+")

print(file.readlines())

place = ["\nCity1: Hisar \n","City2 : Gurugram \n","City3 : Chandigarh \n"]

file.seek(0,2)

file.writelines(place)
print(file.readlines())

file.seek(0,0)
print(file.readlines())

'''
for each in readdata:
    print(each)
'''
file.close()
