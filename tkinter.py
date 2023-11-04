import tkinter as tk
import tut7

mainscreen = tk.Tk()
mainscreen.geometry("300x450")

def printData():
    fname = fname_entry.get()
    lname = lname_entry.get()
    Fname = Fname_entry.get()
    mname = mname_entry.get()
    date = Date.get()
    month = Month.get()
    year = Year.get()

    print()
    print("Check your Details")
    print()
    print("Your Name : "+fname+" "+lname)
    print("Father's Name : Mr. "+Fname)
    print("Mother's Name : Mrs. "+mname)

    if(radiobtn.get()==1):
        print("You are a Male.")
    elif(radiobtn.get()==2):
        print("You are a Female.")
    elif(radiobtn.get()==3):
        print("You are a Transgender.")

    print("Your Date of Birth : ",date,"-",month,"-",year)

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
fname.place (x = 35, y = 75)
fname_entry = tk.Entry(mainscreen, bd = 5,textvariable = "fname")
fname_entry.place(x = 125, y = 75)

lname = tk.Label(mainscreen,text = "Last Name : ")
lname.place (x = 35, y = 120)
lname_entry = tk.Entry(mainscreen, bd = 5,textvariable = "lname")
lname_entry.place(x = 125, y = 120)

Fname = tk.Label(mainscreen,text = "Father's Name : ")
Fname.place (x = 35, y = 160)
Fname_entry = tk.Entry(mainscreen, bd = 5,textvariable = "Fname")
Fname_entry.place(x = 125, y = 160)

mname = tk.Label(mainscreen,text = "Mother's Name : ")
mname.place (x = 35, y = 200)
mname_entry = tk.Entry(mainscreen, bd = 5)
mname_entry.place(x = 125, y = 200)

gen = tk.Label(mainscreen,text = "Gender : ")
gen.place (x = 35, y = 240)
radiobtn = tk.IntVar()
radiobtn1 = tk.Radiobutton (mainscreen, text = "Male",variable = radiobtn, value = 1)
radiobtn1.place(x = 100, y = 240)
radiobtn2 = tk.Radiobutton (mainscreen, text = "Female",variable = radiobtn, value = 2)
radiobtn2.place(x = 150, y = 240)
radiobtn3 = tk.Radiobutton (mainscreen, text = "Other",variable = radiobtn, value = 3)
radiobtn3.place(x = 220, y = 240)

DOB = tk.Label(mainscreen,text = "Date of Birth : ")
DOB.place (x = 35, y = 280)

date = ['01','02','03','04','05','06','07','08','09',10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
Date = tk.StringVar(mainscreen)
Date.set("DD")  
dropdown = tk.OptionMenu(mainscreen, Date, *date)
dropdown.place(x = 110, y = 280)

month = ['01','02','03','04','05','06','07','08','09',10,11,12]
Month = tk.StringVar(mainscreen)
Month.set("MM")  
dropdown = tk.OptionMenu(mainscreen, Month, *month)
dropdown.place(x = 175, y = 280)

year = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005]
Year = tk.StringVar(mainscreen)
Year.set("YYYY")  
dropdown = tk.OptionMenu(mainscreen, Year, *year)
dropdown.place(x = 225, y = 280)

lang = tk.Label(mainscreen,text = "Interests : ")
lang.place (x = 35, y = 320)

checkbox1_var = tk.IntVar()
checkbox1 = tk.Checkbutton(mainscreen,text = "Studies", variable = checkbox1_var, onvalue = 1, offvalue = 0)
checkbox1.place(x = 100,y = 320)

checkbox2_var = tk.IntVar()
checkbox2 = tk.Checkbutton(mainscreen,text = "Supports", variable = checkbox2_var, onvalue = 1, offvalue = 0)
checkbox2.place(x = 175,y = 320)


exitbtn = tk.Button(mainscreen, text = "Exit",background = "Purple",foreground = "white",width = "15",height = "1",activebackground = "pink", command = ext)
exitbtn.place(x = 18,y = 380)

submitbtn = tk.Button(mainscreen, text = "Submit",background = "Purple",foreground = "white",width = "15",height = "1",activebackground = "pink", command = printData)
submitbtn.place(x = 165,y = 380)



mainscreen.mainloop()


