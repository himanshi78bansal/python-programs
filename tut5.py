'''
Write a program to create your profile(name, add, contact, dob, mother name, father name)
1.	all info should be input in runtime
2.	all info should be in well format
3.	all info should be display after entry
4.	file name should be entered by user at runtime
5.	file extension should be given by user
'''

#create your profile

file_name = input("Enter a file name: ")
file_ext = input("Enter a file extension: ")

name = input("Enter your Name: ")
fname = input("Enter your Father's Name: ")
mname = input("Enter your Mother's Name: ")
dob = input("Enter your DOB (in DD/MM/YYYY format): ")
cont = input("Enter your Cont. number: ")
add = input("Enter your Address: ")

# f is used to format the output profile information
profile = f"Name: {name}\nFather's Name: {fname}\nMother's Name: {mname}\nDate of Birth: {dob}\nContact: {cont}\nAddress: {add}"

#write in the file
with open(f"{file_name}.{file_ext}", "w") as file:
    file.write(profile)

#print from the file
print("\nYour profile information:",profile)
