'''
import tkinter as tk

mainscreen = tk.Tk()
mainscreen.geometry("300x350")

def printData():
    print("\nCheck your Details\n")
    print("Your fname : ",fname_entry.get())
    print("Your lname : ",lname_entry.get())
    print("Course :  ",course_entry.get())

    if(radiobtn.get()==1):
        print("You are a Male.")
    elif(radiobtn.get()==2):
        print("You are a Female.")
    else:

        print("You are a Transgender")
        
    if(checkbox1_var.get() == 1):
        if(checkbox1_var.get() == 1 and checkbox2_var.get() == 1):
            print("You are good in Studies as well as Sports")
        else:
            print("You are good in Studies")        
    elif(checkbox2_var.get() == 1):
        print("You are good in Sports")
    else:
        print("you are FUDDU person")
        
        
def ext():
       exit()       

title = tk.Label(mainscreen,text = "Registration Form")
title.place (x = 90, y = 30)

fname = tk.Label(mainscreen,text = "First Name : ")
fname.place (x = 35, y = 80)
fname_entry = tk.Entry(mainscreen, bd = 5)
fname_entry.place(x = 125, y = 80)

lname = tk.Label(mainscreen,text = "Last Name : ")
lname.place (x = 35, y = 120)
lname_entry = tk.Entry(mainscreen, bd = 5)
lname_entry.place(x = 125, y = 120)

course = tk.Label(mainscreen,text = "Course : ")
course.place (x = 35, y = 160)
course_entry = tk.Entry(mainscreen, bd = 5)
course_entry.place(x = 125, y = 160)

gen = tk.Label(mainscreen,text = "Gender : ")
gen.place (x = 35, y = 200)
radiobtn = tk.IntVar()
radiobtn1 = tk.Radiobutton (mainscreen, text = "Male",variable = radiobtn, value = 1)
radiobtn1.place(x = 100, y = 200)
radiobtn2 = tk.Radiobutton (mainscreen, text = "Female",variable = radiobtn, value = 2)
radiobtn2.place(x = 150, y = 200)

lang = tk.Label(mainscreen,text = "Interests : ")
lang.place (x = 35, y = 240)

checkbox1_var = tk.IntVar()
checkbox1 = tk.Checkbutton(mainscreen,text = "Studies", variable = checkbox1_var, onvalue = 1, offvalue = 0)
checkbox1.place(x = 100,y = 240)

checkbox2_var = tk.IntVar()
checkbox2 = tk.Checkbutton(mainscreen,text = "Supports", variable = checkbox2_var, onvalue = 1, offvalue = 0)
checkbox2.place(x = 175,y = 240)


exitbtn = tk.Button(mainscreen, text = "Exit",background = "Purple",foreground = "white",width = "15",height = "1",activebackground = "pink", command = ext)
exitbtn.place(x = 18,y = 300)

submitbtn = tk.Button(mainscreen, text = "Submit",background = "Purple",foreground = "white",width = "15",height = "1",activebackground = "pink", command = printData)
submitbtn.place(x = 165,y = 300)

mainscreen.mainloop()
'''

import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# create a table called 'users'
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name text, email text, password text)''')

# get input from user
name = input('Enter your name: ')
email = input('Enter your email: ')
password = input('Enter your password: ')

# insert user details into the 'users' table
c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))

# commit the changes
conn.commit()

# close the connection
conn.close()






