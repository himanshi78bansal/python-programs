file = open("file.txt","w")

print("file name",file.name)
print("mode",file.mode)

file.writelines("Hello World! \n"),
file.write("I'm learning file handling in python")

file.close()
